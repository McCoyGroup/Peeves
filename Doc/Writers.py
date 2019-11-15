"""
Implements a set of writer classes that document python objects
"""
import abc, os, sys, types

__all__ = [
    "DocWriter",
    "ModuleWriter",
    "ClassWriter",
    "FunctionWriter",
    "ObjectWriter",
    "IndexWriter"
]

class DocWriter(metaclass=abc.ABCMeta):
    "A general writer class that writes a file based off a template and filling in object template specs"

    template = ""
    def __init__(self, obj, out_file, root = None):
        """
        :param obj:
        :type obj:
        :param out_file:
        :type out_file:
        """
        self.obj = obj
        if out_file is None:
            out_file = sys.stdout
        elif isinstance(out_file, str) and os.path.isdir(out_file):
            if root is None:
                root = out_file
            out_file = os.path.join(out_file, *self.identifier.split("."))+".md"
        self.target = out_file
        self.root = root

    class outStream:
        def __init__(self, file, mode = 'w+', **kw):
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
    @property
    def out(self):
        return self.outStream(self.target)
    def write_string(self, txt):
        return self.out.write(txt)

    @abc.abstractmethod
    def template_params(self):
        ...

    def format(self, template = None):
        if template is None:
            template = self.template

        return template.format(**self.template_params())
    def write(self, template = None):
        return self.write_string(self.format(template = template))

    @classmethod
    def load_template(cls, file):
        with open(file) as f:
            return f.read()

    @classmethod
    def get_identifier(cls, o):

        try:
            pkg = o.__module__
        except AttributeError:
            pkg = ""

        try:
            n = o.__qualname__
        except AttributeError:
            try:
                n = o.__name__
            except AttributeError:
                n = type(o).__name__

        qn = pkg + ('.' if pkg != "" else "") + n

        return qn
    @property
    def identifier(self):
        return self.get_identifier(self.obj)

    def load_examples(self):
        if self.root is not None:
            examples = os.path.join(self.root, "examples", self.identifier + ".md")
            if os.path.isfile(examples):
                with open(examples) as f:
                    return f.read()

    ## Markdown utilities

    def format_item(self, item, item_level = 0):
        return "{}- {}".format('  ' * (item_level + 1), item)
    def format_link(self, alt, link):
        return '[{}]({})'.format(alt, link)
    def format_obj_link(self, spec):
        return self.format_link(spec.split('.')[-1], spec.replace('.', '/') + ".md")
    def format_inline_code(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+1)
        return fence + arg + fence
    def format_code_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """
        nticks = arg.count("`")
        fence = "`"*(nticks+3)
        return fence + "python\n" + arg + "\n" + fence

    def format_quote_block(self, arg):
        """

        :param arg:
        :type arg: str
        :return:
        :rtype:
        """

        return ">" + arg.replace("\n", "\n>")

    param_template = """  - `{name}`: `{type}`\n    >{description}"""
    def parse_doc(self, doc):
        """

        :param doc:
        :type doc: str
        :return:
        :rtype:
        """
        from collections import deque

        # parses a docstring based on reStructured text type specs but Markdown description
        splits = doc.strip().splitlines()

        params = deque()
        param_map = {}
        i = len(splits)-1
        for i in range(len(splits)-1, -1, -1):
            line = splits[i].strip()
            if line.startswith(":"):
                if line.startswith(":param"):
                    bits = line.split(":", 2)[1:]
                    name = bits[0][5:].strip()
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"Any", "description":"No description..."}
                    desc = bits[1].strip() if len(bits) == 2 else ""
                    if len(desc) > 0:
                        param_map[name]["description"] = desc
                elif line.startswith(":type"):
                    bits = line.split(":", 2)[1:]
                    name = bits[0][4:].strip()
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"Any", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["type"] = t
                elif line.startswith(":return"):
                    bits = line.split(":", 2)[1:]
                    name = ":returns"
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"_", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["description"] = t
                elif line.startswith(":rtype"):
                    bits = line.split(":", 2)[1:]
                    name = ":returns"
                    if name not in param_map:
                        params.appendleft(name)
                        param_map[name] = {"name":name, "type":"_", "description":"No description..."}
                    t = bits[1].strip() if len(bits) == 2 else ""
                    if len(t) > 0:
                        param_map[name]["type"] = t
            else:
                i = i+1
                break

        param = []
        for p in params:
            param.append(self.param_template.format(**param_map[p]).strip())

        desc = splits[:i]

        return "\n".join(param), "\n".join(desc)


class ModuleWriter(DocWriter):
    """A writer targeted to a module object. Just needs to write the Module metadata."""

    template = DocWriter.load_template(os.path.join(os.path.dirname(__file__), 'templates', 'module.md'))
    def template_params(self):
        import types

        mod = self.obj # type: types.ModuleType
        ex = self.load_examples()
        name = mod.__name__
        ident = self.identifier
        ident_depth = len(ident.split("."))
        mems = [
            self.format_item(self.format_obj_link(
                ".".join(
                    DocWriter.get_identifier(getattr(mod, a)).split(".")[ident_depth-1:]
                )
            )) for a in self.get_members(mod)
        ]
        descr = mod.__doc__ if mod.__doc__ is not None else ''
        return {
            'id' : ident,
            'description' : descr.strip(),
            'name': name,
            'members' : "\n".join(mems),
            'examples' : ex if ex is not None else ""
        }

    @classmethod
    def get_members(cls, mod):
        return (mod.__all__ if hasattr(mod, '__all__') else [])

class ClassWriter(DocWriter):
    """A writer targeted to a class"""
    template = DocWriter.load_template(os.path.join(os.path.dirname(__file__), 'templates', 'class.md'))

    def load_methods(self, function_writer = None):
        import types

        if function_writer is None:
            function_writer = FunctionWriter

        cls = self.obj
        keys = cls.__all__ if hasattr(cls, '__all__') else list(cls.__dict__.keys())

        props = []
        methods = []

        for k in keys:
            o = getattr(cls, k)
            if isinstance(o, types.FunctionType):
                if not k.startswith("_") or (k.startswith("__") and k.endswith("__")):
                    methods.append(function_writer(o, out_file=None, root=self.root).format().strip())
            else:
                if not k.startswith("_"):
                    props.append(self.format_prop(k, o).strip())

        return props, methods

    def format_prop(self, k, o):
        return '{}: {}'.format(k, type(o).__name__)

    def template_params(self, function_writer = None):

        cls = self.obj # type: type
        ex = self.load_examples()
        name = cls.__name__
        ident = self.identifier
        props, methods = self.load_methods(function_writer = function_writer)
        param, descr = self.parse_doc(cls.__doc__ if cls.__doc__ is not None else '')
        descr = descr.strip()
        param = param.strip()
        if len(param) > 0:
            param = "\n" + param
        props = "\n".join(props)
        if len(props) > 0:
            props = self.format_code_block(props)+"\n"

        return {
            'id' : ident,
            'name': name,
            'description' : descr,
            'parameters' : param,
            'props' : props,
            'methods' : "\n\n".join(methods),
            'examples' : ex if ex is not None else ""
        }

class FunctionWriter(DocWriter):
    template = DocWriter.load_template(os.path.join(os.path.dirname(__file__), 'templates', 'function.md'))

    def template_params(self):
        import inspect

        f = self.obj # type: types.FunctionType
        ident = self.identifier
        signature = str(inspect.signature(f))
        name = f.__name__
        param, descr = self.parse_doc(f.__doc__ if f.__doc__ is not None else '')
        descr = descr.strip()
        param = param.strip()
        if len(param) > 0:
            param = "\n" + param
        ex = self.load_examples()
        return {
            'id': ident,
            'name' : name,
            'signature' : signature,
            'parameters' : param,
            'description' : descr,
            'examples' : ex if ex is not None else ""
        }

class ObjectWriter(DocWriter):
    template = DocWriter.load_template(os.path.join(os.path.dirname(__file__), 'templates', 'object.md'))

    @property
    def identifier(self):
        try:
            qualname = self.obj.__qualname__
        except AttributeError:
            qualname = self.get_identifier(type(self.obj)) + "." + self.get_name()
        return qualname
    def get_name(self):
        try:
            name = self.obj.__name__
        except AttributeError:
            name = "<Instance>"

        return name

    def template_params(self):

        try:
            descr = self.obj.__doc__
        except AttributeError:
            descr = "instance of "+type(self.obj).__name__

        if descr is None:
            descr = ''

        ex = self.load_examples()
        return {
            'id': self.identifier,
            'name' : self.get_name(),
            'description' : descr.strip(),
            'examples' : ex if ex is not None else ""
        }

class IndexWriter(DocWriter):
    template = DocWriter.load_template(os.path.join(os.path.dirname(__file__), 'templates', 'index.md'))

    def get_file_paths(self):
        rl = len(os.path.split(self.root))
        fs = [ "/".join(os.path.split(f)[rl-1:]) for f in self.obj ]
        return fs

    def template_params(self):
        files = [ self.format_item(self.format_link(os.path.splitext(f.split("/")[-1])[0], f)) for f in self.get_file_paths()]
        return {
            'index_files' : "\n".join(files)
        }