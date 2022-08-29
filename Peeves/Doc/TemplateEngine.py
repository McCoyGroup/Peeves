import sys, os, abc, enum, types, string
import ast, functools, re, fnmatch, collections
from typing import *

from .ObjectWalker import *

__all__ = [
    "TemplateFormatter",
    "TemplateFormatDirective",

]

class TemplateOps:
    @staticmethod
    def loop(template: str, *args, slots=None, joiner="", formatter=None):
        if slots is not None:
            return joiner.join(
                template.format_map({s: v for s, v in zip(slots, a)}) for a in zip(*args)
            )
        else:
            return joiner.join(
                template.format(*a) for a in zip(*args)
            )
    @staticmethod
    def join(*args, joiner=" ", formatter=None):
        return joiner.join(args)
    @classmethod
    def load(cls, template, formatter=None):
        return formatter.load_template(template)
    @classmethod
    def apply(cls, template, *args, formatter=None, **kwargs):
        if formatter is None:
            raise ValueError("`{}` can't be `None`".format('formatter'))
        return formatter.format(template, *args, **kwargs)
    @classmethod
    def nonemptty(cls, data, formatter=None):
        return data is not None and len(data) > 0
    @classmethod
    def wrap(cls, fn):
        @functools.wraps(fn)
        def f(*args, formatter=None, **kwargs):
            return fn(*args, **kwargs)
        return f

class TemplateFormatDirective(enum.Enum):
    Loop = "loop", TemplateOps.loop
    Join = "join", TemplateOps.join
    Load = "load", TemplateOps.load
    Apply = "apply", TemplateOps.apply
    NonEmpty = "nonempty", TemplateOps.nonempty

    Str = "str", TemplateOps.wrap(str)
    Int = "int", TemplateOps.wrap(int)
    Float = "float", TemplateOps.wrap(float)
    Round = "round", TemplateOps.wrap(round)
    Len = "len", TemplateOps.wrap(len)
    Dict = "dict", TemplateOps.wrap(dict)
    List = "list", TemplateOps.wrap(list)
    Tuple = "tuple", TemplateOps.wrap(tuple)
    Set = "set", TemplateOps.wrap(set)
    def __init__(self, name, callback=None):
        self.key = name
        if isinstance(callback, str):
            callback = callback.format
        elif isinstance(callback, (staticmethod, classmethod, property)):
            callback = callback.__get__(self)
        self.callback = callback if not isinstance(callback, str) else callback.format
    def _call(self, *data, **kwargs):
        return self.callback(*data, **kwargs)
    @classmethod
    def _keymap(cls):
        if not hasattr(cls, '_keymap_dict'):
            cls._keymap_dict = None
        return cls._keymap_dict
    @classmethod
    def _load(cls, name:str):
        k = cls._keymap()
        if k is None:
            cls._keymap_dict = {c.key:c for c in cls}
            k = cls._keymap_dict
        return k[name]

class TemplateFormatterError(ValueError):
    ...
class TemplateASTEvaluator:
    def __init__(self, formatter, directives, format_parameters):
        self.formatter = formatter
        self.directives = directives
        self.format_parameters = format_parameters
    def evaluate_node(self, node:ast.AST):
        if isinstance(node, ast.Module):
            bits = []
            for e in node.body:
                res = self.evaluate_node(e)
                if res is None:
                    res = ""
                bits.append(str(res))
            return "".join(bits)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            return self.format_parameters[node.id]
        elif isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
            return getattr(self.evaluate_node(node.value), node.attr)
        elif isinstance(node, ast.Assign):
            if len(node.targets) > 1:
                raise TemplateFormatterError("Template assignments are restricted to single reassignments")
            if not isinstance(node.targets[0], ast.Name):
                raise TemplateFormatterError("Template assignments are restricted to variable names")
            self.format_parameters[node.targets[0].id] = self.evaluate_node(node.value)
        elif isinstance(node, ast.Expr):
            return self.evaluate_node(node.value)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.List):
            return [self.evaluate_node(e) for e in node.elts]
        elif isinstance(node, ast.Tuple):
            return tuple(self.evaluate_node(e) for e in node.elts)
        elif isinstance(node, ast.Set):
            return {self.evaluate_node(e) for e in node.elts}
        elif isinstance(node, ast.Dict):
            return {self.evaluate_node(k):self.evaluate_node(v) for k,v in zip(node.keys, node.values)}
        elif isinstance(node, ast.BinOp):
            left = self.evaluate_node(node.left)
            right = self.evaluate_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
            elif isinstance(node.op, ast.FloorDiv):
                return left // right
            elif isinstance(node.op, ast.MatMult):
                return left @ right
            elif isinstance(node.op, ast.And):
                return left and right
            elif isinstance(node.op, ast.Or):
                return left or right
            elif isinstance(node.op, ast.BitOr):
                return left | right
            elif isinstance(node.op, ast.BitAnd):
                return left & right
            elif isinstance(node.op, ast.Pow):
                return left ** right
            else:
                raise TemplateFormatterError("unsupported operation {}".format(ast.dump(node.op)))
        elif isinstance(node, ast.Compare):
            left = self.evaluate_node(node.left)
            op = node.ops[0]
            right = self.evaluate_node(node.comparators[0])
            if isinstance(op, ast.Eq):
                return left == right
            elif isinstance(op, ast.NotEq):
                return left != right
            elif isinstance(op, ast.Lt):
                return left < right
            elif isinstance(op, ast.Gt):
                return left > right
            elif isinstance(op, ast.LtE):
                return left <= right
            elif isinstance(op, ast.GtE):
                return left >= right
            elif isinstance(op, ast.In):
                return left in right
            elif isinstance(op, ast.NotIn):
                return left not in right
            elif isinstance(op, ast.Is):
                return left is right
            elif isinstance(op, ast.IsNot):
                return left is not right
            else:
                raise TemplateFormatterError("unsupported comparison {}".format(ast.dump(op)))
        elif isinstance(node, ast.IfExp):
            if self.evaluate_node(node.test):
                return self.evaluate_node(node.body)
            else:
                return self.evaluate_node(node.orelse)


            # IfExp(
            #     test=Compare(left=Constant(value=1, kind=None), ops=[Gt()], comparators=[Constant(value=2, kind=None)]),
            #     body=Name(id='add_temp', ctx=Load()), orelse=Constant(value='', kind=None))
            # unsupported

        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute): # subattr of some object...I guess we can call it?
                directive = self.evaluate_node(node.func)
            directive = None
            if isinstance(node.func, ast.Name):
                name = node.func.id
                directive = self.directives._load(name)
            if directive is None:
                directive = self.evaluate_node(node.func)
            else:
                directive = lambda *a,_d=directive,**k:_d._call(*a, formatter=self.formatter, **k)
            args = [self.evaluate_node(a) for a in node.args]
            kwargs = {k.arg: self.evaluate_node(k.value) for k in node.keywords}
            return directive(*args, **kwargs)
        else:
            raise TemplateFormatterError("Node {} unsupported".format(ast.dump(node)))
class TemplateFormatter(string.Formatter):
    """
    Provides a formatter for fields that allows for
    the inclusion of standard Bootstrap HTML elements
    alongside the classic formatting
    """
    directives = TemplateFormatDirective
    class frozendict(dict):
        def __setitem__(self, key, value):
            raise TypeError("`frozendict` is immutable")
    def __init__(self, templates):
        self.__templates = self.frozendict(templates)
        self.format_parameters = None
    @property
    def templates(self):
        return self.__templates
    @property
    def callback_map(self):
        return dict(
            {"$":self.apply_directive_tree},
            **{d.key+"$":self.apply_directive for d in self.directives}
        )
    def apply_directive_tree(self, _, spec) -> str:
        tree = ast.parse("("+spec+")")
        ev = TemplateASTEvaluator(self, self.directives, self.format_parameters).evaluate_node(tree)
        if ev is None:
            ev = ""
        return ev
    def apply_directive(self, key, spec) -> str:
        return self.apply_directive_tree(
            key,
            "{}({})".format(key.strip("$"), spec)
        )
    def format_field(self, value: Any, format_spec: str) -> str:
        callback = (
            self.callback_map.get(value, None)
            if isinstance(value, str)
            else None
        )
        if callback is None:
            return super().format_field(value, format_spec)
        else:
            return callback(value, format_spec)

    _template_cache = {}
    def load_template(self, template):
        if template not in self.__templates:
            raise ValueError("can only load templates that ")
        template = self.templates[template]
        if os.path.exists(template):
            if template not in self._template_cache:
                with open(template) as file:
                    template = file.read()
                self._template_cache[template] = template
            else:
                template = self._template_cache[template]
        return template

        # if value in s
        #     ...
        # else:
        #     super()
        # directive, args = self.parse_spec(format_spec)
        # self.directives(directive).apply(
        #     value, *args
        # )

    def vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]):
        try:
            self.format_parameters = kwargs.copy()
            if "$" not in kwargs:
                kwargs["$"] = "$"
            for d in self.directives:
                if d.key+"$" not in kwargs:
                    kwargs[d.key+"$"] = d.key+"$"
            return super().vformat(format_string, args, kwargs)
        finally:
            self.format_parameters = None

class ResourcePathLocator:
    def __init__(self, path:Iterable[str]):
        self.path = list(path)
    def locate(self, identifier):
        if os.path.exists(identifier):
            return os.path.abspath(identifier)
        else:
            for d in self.path:
                f = self.resource_path(d, identifier)
                if os.path.exists(f):
                    return f
    def resource_path(self, d, f):
        return os.path.join(d, f)
    def paths(self):
        s = None
        for d in self.path:
            dirs = os.listdir(self.resource_path(d, ""))
            if s is None:
                s = set(dirs)
            else:
                s = s.union(dirs)
        return s
class SubresourcePathLocator(ResourcePathLocator):
    def __init__(self, roots, extension):
        self.ext = extension
        super().__init__(roots)
    def resource_path(self, d, f):
        return os.path.join(d, self.ext, f)
class ResourceLocator:
    def __init__(self,
                 locators:Iterable[Union[ResourcePathLocator,Iterable[str],Tuple[Iterable[str], str]]]
                 ):
        self.locators = [
            s if isinstance(s, ResourcePathLocator)
            else ResourcePathLocator(s) if isinstance(s[0], str)
            else SubresourcePathLocator(*s)
            for s in locators
        ]
    def locate(self, identifier):
        for l in self.locators:
            res = l.locate(identifier)
            if res is not None:
                return res
    def paths(self, filter_pattern=None):
        paths = {r for l in self.locators for r in l.paths()}
        if filter_pattern is not None:
            if isinstance(filter_pattern, str):
                try:
                    filter_pattern = re.compile(filter_pattern)
                except ValueError:
                    filter_pattern = re.compile(fnmatch.translate(filter_pattern))
            paths = {p for p in paths if filter_pattern.match(p)}
        return paths

class TemplateEngine:
    """
    Provides an engine for generating content using a
    `TemplateFormatter` and `ResourceLocator`, but does not handle
    any writing of files
    """

    def __init__(self,
                 locator:ResourceLocator,
                 template_pattern="*.*",
                 ignore_missing=False,
                 ignore_paths=()
                 ):
        self.locator = locator
        self.templates = {
            k:self.locator.locate(k)
            for k in self.locator.paths(filter_pattern=template_pattern)
        }
        self.formatter = TemplateFormatter(self.templates)
        self.ignore_missing = ignore_missing
        self.ignore_paths = ignore_paths

    def format_map(self, template, parameters):
        if template in self.templates:
            template = self.formatter.load_template(template)
        return self.formatter.vformat(
            template,
            (),
            parameters if not self.ignore_missing else collections.defaultdict(parameters)
        )
    def format(self, template, **parameters):
        return self.format_map(template, parameters)

    class outStream:
        def __init__(self, file, mode='w+', **kw):
            self.file = file
            self.file_handle = None
            self.mode = mode
            self.kw = kw

        def __enter__(self):
            if self.file_handle is None:
                if isinstance(self.file, str):
                    try:
                        os.makedirs(os.path.dirname(self.file))
                    except OSError:
                        pass
                    self.file_handle = open(self.file, self.mode, **self.kw)
                else:
                    self.file_handle = self.file
            return self.file_handle

        def __exit__(self, exc_type, exc_val, exc_tb):
            if isinstance(self.file, str):
                self.file_handle.close()
            self.file_handle = None

        def write(self, s):
            with self as out:
                out.write(s)
            return self.file
    def write_string(self, target, txt):
        return self.outStream(target).write(txt)
    def apply(self, template, target, **template_params):
        if target not in self.ignore_paths:
            return self.write_string(
                target,
                self.format_map(template, template_params)
            )

class TemplateHandler(ObjectHandler):
    template = None
    extension = ".md"
    def __init__(self,
                 obj,
                 out_file,
                 engine:TemplateEngine,
                 root=None,
                 **extra_fields
                 ):
        super().__init__(obj, **extra_fields)
        if out_file is None:
            out_file = sys.stdout
        elif isinstance(out_file, str) and os.path.isdir(out_file):
            if root is None:
                root = out_file
            out_file = os.path.join(root, *self.identifier.split("."))+self.extension
        self.target = out_file
        if root is None:
            root = os.path.dirname(self.target)
        self.root = root
        self.engine = engine

    def template_params(self, **kwargs):
        base_parms = self.extra_fields.copy()
        base_parms.update(self.get_template_params(**kwargs))
        return base_parms
    @abc.abstractmethod
    def get_template_params(self, **kwargs):
        """
        Returns the parameters that should be inserted into the template

        :return:
        :rtype: dict
        """
        raise NotImplementedError("abstract base class")

    def handle(self, template=None, target=None):
        """
        Formats the documentation Markdown from the supplied template

        :param template:
        :type template:
        :return:
        :rtype:
        """
        if self.check_should_write():
            if template is None:
                template = self.template
            params = self.template_params()
            if target is None:
                out_file = self.target
            else:
                out_file = target
            if isinstance(out_file, str):
                pkg, file_url = self.package_path
                params['package_name'] = pkg
                params['file_url'] = file_url
                params['package_url'] = os.path.dirname(file_url)

                if self.root is not None:
                    root_split = []
                    root = self.root
                    while root and (root != "/" and root != os.path.pathsep):
                        root, base = os.path.split(root)
                        root_split.append(base)
                    out_split = []
                    out = out_file
                    while out and (out != "/" and out != os.path.pathsep):
                        out, base = os.path.split(out)
                        out_split.append(base)
                    out_split = list(reversed(out_split))
                    root_depth = len(root_split)
                    out_url = "/".join(out_split[root_depth:])
                    # print(os.path.split(out_file), root_depth)
                else:
                    out_url = "/".join(os.path.split(out_file)[-len(os.path.split(file_url))])
                params['file'] = out_file
                params['url'] = out_url

            try:
                out = self.engine.apply(template, out_file, **params)
            except KeyError as e:
                raise ValueError("{} ({}): template needs key {}".format(
                    type(self).__name__,
                    self.obj,
                    e.args[0]
                ))
            except IndexError as e:
                raise ValueError("{} ({}): template index {} out of range...".format(
                    type(self).__name__,
                    self.obj,
                    e.args[0]
                ))
            return out

    blacklist_packages = {"builtins", 'numpy', 'scipy', 'matplotlib'} #TODO: more sophisticated blacklisting
    def check_should_write(self):
        """
        Determines whether the object really actually should be
        documented (quite permissive)
        :return:
        :rtype:
        """
        return self.identifier.split(".", 1)[0] not in self.blacklist_packages

class ModuleTemplateHandler(TemplateHandler):
    template = 'module.md'
class ClassTemplateHandler(TemplateHandler):
    template = 'class.md'
class FunctionTemplateHandler(TemplateHandler):
    template = 'function.md'
class MethodTemplateHandler(TemplateHandler):
    template = 'method.md'
class ObjectTemplateHandler(TemplateHandler):
    template = 'object.md'
class IndexTemplateHandler(TemplateHandler):
    template = 'index.md'

class TemplateWalker(ObjectWalker):
    module_handler = ModuleTemplateHandler
    class_handler = ClassTemplateHandler
    function_handler = FunctionTemplateHandler
    method_handler = MethodTemplateHandler
    object_handler = ObjectTemplateHandler
    index_handler = IndexTemplateHandler
    def __init__(self, engine:TemplateEngine, out=None, **extra_fields):
        self.engine = engine
        self.out_dir = out
        super().__init__(**extra_fields)

    @property
    def default_handlers(self):
        return collections.OrderedDict((
            ((str, types.ModuleType), self.module_handler),
            ((type,), self.class_handler),
            ((types.FunctionType,), self.function_handler)
        ))

    def get_handler(self, *args, tree=None, **kwargs):
        return super().get_handler(
            *(args + (self.out_dir, self.engine)),
            tree=tree,
            **kwargs
        )

    def write(self, objects, index='index.md'):
        """
        Walks through the objects supplied and applies the appropriate templates
        :return: index of written files
        :rtype: str
        """

        if self.out_dir is not None and index is not None:
            try:
                os.makedirs(self.out_dir)
            except OSError:
                pass
            out_file = os.path.join(self.out_dir, index)
        else:
            out_file = None

        files = [self.visit(o) for o in objects]
        files = [f for f in files if f is not None]
        w = self.index_handler(files,
                               out_file,
                               self.engine,
                               root=self.out_dir,
                               extra_fields=self.extra_fields
                               )
        return w.handle()