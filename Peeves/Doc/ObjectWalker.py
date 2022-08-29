
"""
Provides a class that will walk through a set of objects & their children, as loaded into memory,
and call appropriate handlers for each
"""

import os, types, collections, abc
import sys, importlib
# from .Writers import *

__all__ = [
    "ObjectWalker",
    "ObjectHandler"
]

class ObjectTree(dict):
    """
    Simple tree that stores the structure of the documentation
    """
class ObjectSpec(dict):
    required_keys = ['id']

class MethodDispatch(collections.OrderedDict):
    """
    Provides simple utility to dispatch methods based on types
    """

    def __init__(self, *args, default=None, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)
    class DispatchTests:
        def __init__(self, *tests):
            self.tests = tests
        def __hash__(self):
            return self.tests.__hash__()
        def __call__(self, obj):
            return all(self.test(t, obj) for t in self.tests)
        @classmethod
        def test(cls, k, obj):
            """
            Does the actual dispatch testing

            :param k:
            :type k:
            :param obj:
            :type obj:
            :return:
            :rtype:
            """
            if (
                    isinstance(k, type) or
                    isinstance(k, tuple) and all(isinstance(kk, type) for kk in k)
            ):
                return isinstance(obj, k)
            elif isinstance(k, str):
                return hasattr(obj, k)
            elif isinstance(k, tuple) and all(isinstance(kk, str) for kk in k):
                return any(hasattr(obj, kk) for kk in k)
            elif isinstance(k, tuple):
                return any(kk(obj) for kk in k)
            else:
                return k(obj)
    def method_dispatch(self, obj, *args, **kwargs):
        """
        A general-ish purpose type or duck-type method dispatcher.

        :param obj:
        :type obj:
        :param table:
        :type table:
        :return:
        :rtype:
        """

        for k, v in self.items():
            if isinstance(k, self.DispatchTests):
                matches = k(obj)
            else:
                matches = self.DispatchTests.test(k, obj)
            if matches:
                return v(obj, *args, **kwargs)

        if self.default is None:
            raise TypeError("object {} can't dispatch from table {}".format(
                obj, self
            ))
        else:
            return self.default(obj, *args, **kwargs)
    def __call__(self, obj, *args, **kwargs):
        return self.method_dispatch(obj, *args, **kwargs)
    def __setitem__(self, key, value):
        """
        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        #TODO: make dispatch keys automatically feed into
        if isinstance(key, tuple):
            # make sure we're not just doing alternatives
            if not (
                    all(isinstance(k, str) for k in key) or
                    all(isinstance(k, type) for k in key) or
                    all(callable(k) for k in key)
            ):
                # then we do, basically, an 'and' operand
                key = self.DispatchTests(*key)
        super().__setitem__(key, value)

class ObjectHandler(metaclass=abc.ABCMeta):
    def __init__(self,
                 obj,
                 spec=None,
                 tree=None,
                 name=None,
                 parent=None,
                 walker=None,
                 **extra_fields
                 ):

        self.walker = walker
        self.obj = obj
        self._id = None
        self._name = name
        self._parent = parent
        self._pobj = None
        self._chobj = None
        self.spec = spec
        self.tree = tree

        self.extra_fields = extra_fields

    @property
    def name(self):
        """
        Returns the name (not full identifier) of the object
        being documented

        :return:
        :rtype:
        """
        return self.get_name()

    def get_name(self):
        """
        Returns the name the object will have in its documentation page

        :return:
        :rtype:
        """
        if self._name is not None:
            name = self._name
        else:
            try:
                name = self.obj.__name__
            except AttributeError:
                name = "<{} Instance>".format(type(self.obj).__name__)

        return name

    def get_package_and_url(self):
        """
        Returns package name and corresponding URL for the object
        being handled

        :return:
        :rtype:
        """
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
        if self._id is None:
            self._id = self.get_identifier(self.obj)
        return self._id

    @property
    def parent(self):
        """
        Returns the parent object for docs purposes

        :return:
        :rtype:
        """
        if self._pobj is None:
            self._pobj = self.resolve_parent()
        return self._pobj
    def resolve_parent(self, check_tree=True):
        """
        Resolves the "parent" of obj.
        By default, just the module in which it is contained.
        Allows for easy skipping of pieces of the object tree,
        though, since a parent can be directly added to the set of
        written object which is distinct from the module it would
        usually resolve to.
        Also can be subclassed to provide more fine grained behavior.

        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        if check_tree:
            oid = self.identifier
            if self.tree is not None and oid in self.tree:
                return self.tree[oid]['parent']

        if self._parent is not None:
            if isinstance(self._parent, str):
                return self.walker.resolve_object(self._parent)
            else:
                return self._parent
        elif 'parent' in self.spec:
            parent = self.spec['parent']
            if isinstance(parent, str):
                return self.walker.resolve_object(parent)
            else:
                return parent

        if isinstance(self.obj, types.ModuleType):
            # not totally sure this will work...
            modspec = self.obj.__name__.rsplit(".", 1)[0]
        else:
            modspec = self.obj.__module__

        if modspec == "":
            return None

        return self.walker.resolve_object(modspec)

    @property
    def children(self):
        """
        Returns the child objects for docs purposes

        :return:
        :rtype:
        """
        if self._chobj is None:
            self._chobj = self.resolve_children()
        return self._chobj
    def resolve_children(self, check_tree=True):
        """
        Resolves the "children" of obj.
        First tries to use any info supplied by the docs tree
        or a passed object spec, then that failing looks for an
        `__all__` attribute

        :param obj:
        :type obj:
        :return:
        :rtype:
        """

        childs = None
        if check_tree:
            oid = self.identifier
            if self.tree is not None and oid in self.tree:
                childs = self.tree[oid]['children']
        if childs is None:
            if 'children' in self.spec:
                childs = self.spec['children']
            elif hasattr(self.obj, '__all__'):
                childs = self.obj.__all__
            else:
                childs = []

        oid = self.identifier
        return [self.walker.resolve_object(oid + "." + x) if isinstance(x, str) else x for x in childs]

    @property
    def tree_spec(self):
        """
        Provides info that gets added to the `written` dict and which allows
        for a doc tree to be built out.

        :return:
        :rtype:
        """

        base_spec = {
            'id': self.identifier,
            'parent': self.parent,
            'children': self.children
        }
        base_spec.update(self.spec)
        return base_spec

    @abc.abstractmethod
    def handle(self):
        raise NotImplementedError("abstract method")

class ObjectWalker:
    """
    A class that walks a module/object structure, calling handlers
    appropriately at each step

    A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
    and a Markdown index file.

    Takes a set of objects & writers and walks through the objects, generating files on the way
    """

    spec = ObjectSpec
    default_handlers = collections.OrderedDict()
    def __init__(self,
                 handlers=None,
                 tree=None,
                 **extra_fields
                 ):
        """
        :param objects: the objects to write out
        :type objects: Iterable[Any]
        :param out: the directory in which to write the files (`None` means `sys.stdout`)
        :type out: None | str
        :param out: the directory in which to write the files (`None` means `sys.stdout`)
        :type out: None | str
        :param: writers
        :type: DispatchTable
        :param ignore_paths: a set of paths not to write (passed to the objects)
        :type ignore_paths: None | Iterable[str]
        """

        # obtain default writer set
        if handlers is None:
            handlers = {}
        if not isinstance(handlers, MethodDispatch):
            if hasattr(handlers, 'items'):
                handlers = MethodDispatch(handlers.items(), default=ObjectHandler)
            else:
                handlers = MethodDispatch(handlers, default=ObjectHandler)
        for k, v in self._initial_handlers.items():
            if k not in handlers:
                handlers[k] = v
        self.handlers = handlers

        # obtain default tree
        if tree is None:
            tree = ObjectTree()
        self.tree = tree

        self.extra_fields = extra_fields

    @property
    def _initial_handlers(self):
        """
        Adds a minor hook onto the default_writes dict and returns it
        :return:
        :rtype:
        """

        writers = self.default_handlers.copy()
        writers[self.spec] = self.resolve_spec
        return writers

    def get_handler(self, *args, tree=None, **kwargs):
        return self.handlers(*args,
                                **dict(self.extra_fields, tree=self.tree, **kwargs)
                                )
    @staticmethod
    def resolve_object(o):
        """
        Resolves to an arbitrary object by name

        :param o:
        :type o:
        :return:
        :rtype:
        """

        if o in sys.modules:
            # first we try to do a direct look up
            o = sys.modules[o]
        elif o.rsplit(".", 1)[0] in sys.modules:
            # if direct lookup failed, but the parent module has been loaded
            # try direct lookup on that
            try:
                mod, attr = o.rsplit(".", 1)
                o = getattr(sys.modules[mod], attr)
            except AttributeError:
                o = importlib.import_module(o)
        else:
            # otherwise fall back on standard import machinery
            try:
                o = importlib.import_module(o)
            except ModuleNotFoundError:  # tried to load a member but couldn't...
                # we try to resolve this by doing an iterated getattr
                p_split = o.split(".")
                mod_spec = ".".join(p_split[:-1])
                if mod_spec == "":
                    raise ValueError("can't resolve '{}'".format(o))
                try:
                    mood = importlib.import_module(mod_spec)
                    from functools import reduce
                    v = reduce(lambda m, a: getattr(m, a), p_split[1:], mood)
                except ModuleNotFoundError:
                    pass
                else:
                    o = v

        return o

    def resolve_spec(self, spec, *args, **kwargs):
        """
        Resolves an object spec.

        :param spec: object spec
        :type spec: ObjectSpec
        :return:
        :rtype:
        """

        # for the moment we only reolve using the `id` parameter
        oid = spec['id']
        o = self.resolve_object(oid)
        return self.get_handler(o,
                                *args,
                                spec=spec,
                                **kwargs
                                )


    def visit(self, o, parent=None, **kwargs):
        """
        Visits a single object in the tree
        Provides type dispatching to a handler, basically.

        :param o: the object we want to handler
        :type o: Any
        :param parent: the handler that was called right before this
        :type parent: ObjectHandler
        :return: the result of handling
        :rtype: Any
        """

        if (
                isinstance(o, (dict, collections.OrderedDict))
                and all(k in o for k in self.spec.required_keys)
        ):
            o = self.spec(o.items())

        if parent is not None:
            pid = parent.identifier
        else:
            pid = None

        handler = self.get_handler(o,
                                   parent=pid,
                                   **kwargs
                                   )

        oid = handler.identifier
        if oid not in self.tree:
            res = handler.handle()
            if res is not None: # basically means stop writing
                spec = handler.tree_spec
                spec.update(file=res)
                self.tree[oid] = spec

                for child in handler.children:
                    self.visit(child, parent=handler, **dict(handler.extra_fields, **kwargs))
            return res