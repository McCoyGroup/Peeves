"""
Implements a set of writer classes that document python objects
"""
import abc, os, sys, types, inspect, re

__all__ = [
    "DocWriter",
    "ModuleWriter",
    "ClassWriter",
    "FunctionWriter",
    "ObjectWriter",
    "IndexWriter"
]

#TODO: it turns out a lot of this gymnastics can be replaced with the `inspect` module...womp

class DocWriter(metaclass=abc.ABCMeta):
    "A general writer class that writes a file based off a template and filling in object template specs"

    template = "No template :|"
    template_root = "templates"
    template_name = ""
    default_template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    example_root = "examples"
    _template_cache = {}
    def __init__(self,
                 obj, out_file,
                 obj_name = None,
                 parent_obj = None,
                 template = None, root = None, ignore_paths=None):
        """
        :param obj:
        :type obj:
        :param out_file:
        :type out_file:
        """
        self.obj = obj
        self.obj_name = obj_name
        self.parent_obj = parent_obj
        if out_file is None:
            out_file = sys.stdout
        elif isinstance(out_file, str) and os.path.isdir(out_file):
            if root is None:
                root = out_file
            out_file = os.path.join(root, *self.identifier.split("."))+".md"
        self.ignore_paths = ignore_paths if ignore_paths is not None else set()

        # we try to build a template...
        if template is None:
            if root is None:
                root = os.path.dirname(out_file)
            template = os.path.join(root, self.template_root, *self.identifier.split("."))+".md"
            if not os.path.exists(template):
                template = os.path.join(root, self.template_root, self.template_name)
                if not os.path.exists(template):
                    template = os.path.join(root, self.default_template_dir, self.template_name)
            if os.path.exists(template):
                if template in self._template_cache:
                    template = self._template_cache[template]
                else:
                    tkey = template
                    with open(template) as tf:
                        template = tf.read()
                    self._template_cache[tkey] = template
            else:
                template = self.template

        self.template = template
        self.target = out_file
        self.root = root

    def get_name(self):
        try:
            name = self.obj.__name__
        except AttributeError:
            if self.obj_name is None:
                name = "<{} Instance>".format(type(self.obj).__name__)
            else:
                name = self.obj_name

        return name

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

    def _clean_doc(self, doc):
        """
        :param doc: a docstring
        :type doc: str
        :return: a cleaned docstring
        :rtype: str
        """
        # strip off leading whitespace in a uniform manner
        doc = doc.rstrip()
        if len(doc) == 0:
            return doc
        doc_lines = doc.rstrip().splitlines()
        leading_spaces = len(doc_lines[0]) - len(doc_lines[0].lstrip())
        if leading_spaces == 0 and len(doc_lines) > 1: # sometimes there's no leading whitespace depending on how things were written
            leading_spaces = len(doc_lines[1]) - len(doc_lines[1].lstrip())
            for i,d in enumerate(doc_lines[1:]):
                doc_lines[i+1] = doc_lines[i+1][leading_spaces:]
        else:
            for i,d in enumerate(doc_lines):
                doc_lines[i] = doc_lines[i][leading_spaces:]
        return "\n".join(doc_lines)
    def format(self, template = None):
        if template is None:
            template = self.template
        params = self.template_params()
        out_file = self.target
        if isinstance(out_file, str):
            if self.root is not None:
                root_split = []
                root = self.root
                while root:
                    root, base = os.path.split(root)
                    root_split.append(base)
                out_split = []
                out = out_file
                while out:
                    out, base = os.path.split(out)
                    out_split.append(base)
                out_split = list(reversed(out_split))
                root_depth = len(os.path.split(self.root))
                out_url = "/".join(out_split[root_depth:])
                # print(os.path.split(out_file), root_depth)
            else:
                out_url = "/".join(os.path.split(out_file))
            params['file'] = out_file
            params['url'] = out_url

            pkg, file_url = self.package_path
            params['package_name'] = pkg
            params['file_url'] = file_url
        return template.format(**params)
    def write(self, template = None):
        if self.target not in self.ignore_paths:
            return self.write_string(self.format(template = template))

    def get_package_and_url(self):
        pkg_split = self.identifier.split(".", 1)
        if len(pkg_split) == 1:
            pkg = pkg_split[0]
            rest = ""
        elif len(pkg_split) == 0:
            pkg = ""
            rest = "Not.A.Real.Package"
        else:
            pkg, rest = pkg_split
        if len(rest) == 0:
            file_url = "__init__.py"
        else:
            file_url = rest.replace(".", "/") + "/__init__.py"
        return pkg, file_url
    @property
    def package_path(self):
        return self.get_package_and_url()

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
            examples = os.path.join(self.root, self.example_root, *self.identifier.split("."))+".md"
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

    template_name = 'module.md'
    def template_params(self):
        import types

        mod = self.obj # type: types.ModuleType
        ex = self.load_examples()
        name = mod.__name__
        ident = self.identifier
        ident_depth = len(ident.split("."))
        # get identifiers
        idents = [ DocWriter.get_identifier(getattr(mod, a)) for a in self.get_members(mod) ]
        # flattend them
        idents = [ i for i in idents if ident in i ]
        # split by qualified names
        idents = [".".join(a.split(".")[ident_depth-1:]) for a in idents]
        # format links
        mems = [ self.format_item(self.format_obj_link(l)) for l in idents ]
        # print([idents, mems])
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

    template_name = 'class.md'
    def load_methods(self, function_writer = None):
        import types

        if function_writer is None:
            function_writer = MethodWriter

        cls = self.obj
        keys = cls.__all__ if hasattr(cls, '__all__') else list(cls.__dict__.keys())

        props = []
        methods = []

        for k in keys:
            o = getattr(cls, k)
            if isinstance(o, (types.FunctionType, classmethod, staticmethod, property)):
                if not k.startswith("_") or (k.startswith("__") and k.endswith("__")):
                    methods.append(
                        function_writer(o, parent_obj = cls, obj_name = k, out_file=None, root=self.root).format().strip())
            else:
                if not k.startswith("_"):
                    props.append(self.format_prop(k, o).strip())

        return props, methods

    def get_package_and_url(self):
        pkg, rest = self.identifier.split(".", 1)
        rest, bleh = rest.rsplit(".", 1)
        file_url = rest.replace(".", "/") + ".py"
        # lineno = inspect.findsource(self.obj)[1]
        return pkg, file_url #+ "#L" + str(lineno) # for GitHub links

    def format_prop(self, k, o):
        return '{}: {}'.format(k, type(o).__name__)

    def template_params(self, function_writer = None):

        cls = self.obj # type: type
        ex = self.load_examples()
        name = cls.__name__
        ident = self.identifier
        props, methods = self.load_methods(function_writer = function_writer)
        param, descr = self.parse_doc(cls.__doc__ if cls.__doc__ is not None else '')
        descr = self._clean_doc(descr)
        param = self._clean_doc(param)
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

    template_name = 'function.md'

    def get_signature(self):
        return str(inspect.signature(self.obj))
    def template_params(self):

        f = self.obj # type: types.FunctionType
        ident = self.identifier
        signature = self.get_signature()
        mem_obj_pat = re.compile(" object at \w+>")
        signature = re.sub(mem_obj_pat, " instance>", signature)
        name = self.get_name()
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

    def get_package_and_url(self):
        pkg, rest = self.identifier.split(".", 1)
        rest, bleh = rest.rsplit(".", 1)
        file_url = rest.replace(".", "/") + ".py"
        # lineno = inspect.findsource(self.obj)[1]
        return pkg, file_url #+ "#L" + str(lineno) # for GitHub links

class MethodWriter(FunctionWriter):

    template_name = 'method.md'
    def template_params(self):
        params = super().template_params()
        meth = self.obj # type: types.MethodType
        decorator = ""
        if isinstance(meth, classmethod):
            decorator = 'classmethod'
        elif isinstance(meth, property):
            decorator = 'property'
        elif isinstance(meth, staticmethod):
            decorator = 'staticmethod'
        if len(decorator) > 0:
            decorator = "@" + decorator + "\n"
        params['decorator'] = decorator
        return params
    def get_signature(self):
        try:
            signature = str(inspect.signature(self.obj))
        except TypeError:  # dies on properties
            signature = "(self)"
        return signature
    @property
    def identifier(self):
        if isinstance(self.obj, property):
            return self.get_identifier(self.parent_obj) + "." + self.get_name()
        else:
            return self.get_identifier(self.obj)

class ObjectWriter(DocWriter):

    template_name = 'object.md'
    @property
    def identifier(self):
        try:
            qualname = self.obj.__qualname__
        except AttributeError:
            qualname = self.get_identifier(type(self.obj)) + "." + self.get_name()
        qn = qualname.split(".")
        qualname = ".".join(qn[:-2] + qn[-1:]) # want to drop the class name
        # print(qualname)
        return qualname

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

    template_name = 'index.md'
    def get_identifier(cls, o):
        return 'index'

    def get_file_paths(self):
        rl = len(os.path.split(self.root))
        fs = [ "/".join(os.path.split(f)[rl-1:]) for f in self.obj ]
        return fs

    def template_params(self):
        files = [
            self.format_item(
                self.format_link(os.path.splitext(f.split("/")[-1])[0], f)
            ) for f in self.get_file_paths()
        ]
        return {
            'index_files' : "\n".join(files)
        }