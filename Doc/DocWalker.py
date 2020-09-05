"""
Provides a class that will walk through a set of objects & their children, as loaded into memory, and will generate Markdown for each.
The actual object Markdown is written by the things in the `Writers` module.
"""

from .Writers import *
import os

__all__ = [ "DocWalker" ]

class DocWalker:
    """
    A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
    and a Markdown index file.

    Takes a set of objects & writers and walks through the objects, generating files on the way
    """
    def __init__(self,
                 objects,
                 out = None,
                 module_writer = None,
                 class_writer = None,
                 function_writer = None,
                 object_writer = None,
                 ignore_paths = None
                 ):
        """
        :param objects: the objects to write out
        :type objects: Iterable[Any]
        :param out: the directory in which to write the files (`None` means `sys.stdout`)
        :type out: None | str
        :param module_writer: the class to used to write module Markdown (`None` means `ModuleWriter`)
        :type module_writer: type
        :param class_writer: the class to used to write class Markdown(`None` means `ClassWriter`)
        :type class_writer: type
        :param function_writer: the class to used to write function Markdown (`None` means `FunctionWriter`)
        :type function_writer: type
        :param object_writer: the class to used to write object Markdown (`None` means `ObjectWriter`)
        :type object_writer: type
        :param ignore_paths: a set of paths not to write (passed to the objects)
        :type ignore_paths: None | Iterable[str]
        """
        self.objects = objects
        if module_writer is None:
            module_writer = ModuleWriter
        if class_writer is None:
            class_writer = ClassWriter
        if function_writer is None:
            function_writer = FunctionWriter
        if object_writer is None:
            object_writer = ObjectWriter

        self.module_writer = module_writer
        self.class_writer = class_writer
        self.function_writer = function_writer
        self.object_writer = object_writer
        self.ignore_paths = ignore_paths

        if out is None:
            out = os.path.join(os.getcwd(), "Documentation")
        self.out_dir = out
        try:
            os.makedirs(self.out_dir)
        except OSError:
            pass

    def write_object(self, o, written = None):
        import types

        if written is None:
            written = set()

        if isinstance(o, type):
            oid = self.class_writer.get_identifier(o)
            if not oid in written:
                writer = self.class_writer(o, self.out_dir, ignore_paths=self.ignore_paths)
                res = writer.write()
                written.add(oid)
                return res
        elif isinstance(o, types.FunctionType):
            oid = self.function_writer.get_identifier(o)
            if not oid in written:
                writer = self.function_writer(o, self.out_dir, ignore_paths=self.ignore_paths)
                res = writer.write()
                written.add(oid)
                return res
        elif isinstance(o, types.ModuleType) or isinstance(o, str):
            import sys

            if isinstance(o, str):
                if o in sys.modules:
                    # first we try to do a direct look up
                    o = sys.modules[o]
                elif ".".join(o.split(".")[:-1]) in sys.modules:
                    # if direct lookup failed, but the parent module has been loaded, direct lookup that
                    o_split = o.split(".")
                    o_end = o_split[-1]
                    o = getattr(sys.modules[".".join(o_split[:-1])], o_end)
                else:
                    # otherwise fall back on standard import machinery
                    try:
                        o = __import__(o)
                    except ModuleNotFoundError: # tried to load a member but couldn't...
                        # first we see we resolve this by doing an iterated getattr
                        p_split = o.split(".")
                        mod_spec = ".".join(p_split[:-1])
                        try:
                            mood = __import__(mod_spec)
                            from functools import reduce
                            v = reduce(lambda m,a: getattr(m, a), p_split[1:], mood)
                        except ModuleNotFoundError:
                            pass
                        else:
                            o = v
                            #return self.write_object(v, written)

            if isinstance(o, types.ModuleType):
                oid = self.module_writer.get_identifier(o)
                if not oid in written:
                    writer = self.module_writer(o, self.out_dir, ignore_paths=self.ignore_paths)
                    res = writer.write()
                    written.add(oid)

                    mod_split = oid.split(".")
                    for k in self.module_writer.get_members(o):
                        v = getattr(o, k)
                        v_id = self.module_writer.get_identifier(v)
                        # make sure parent dependencies get added
                        v_split = v_id.split(".")
                        for extra in range(len(mod_split), len(v_split)):
                            self.write_object(".".join(v_split[:extra]), written = written)
                        self.write_object(v, written = written)

                    return res
        else:
            t = type(o)
            if t.__module__ in written or ".".join(t.__module__.split(".")[:-1]) in written:
                self.write_object(t, written)
                if hasattr(o, "__doc__") and hasattr(o, "__name__"):
                    w = self.object_writer(o, self.out_dir)
                    oid = w.identifier
                    if not oid in written:
                        res = w.write()
                        written.add(oid)
                        return res

    def write_docs(self):
        files = [ self.write_object(o) for o in self.objects ]
        files = [ f for f in files if f is not None ]
        w = IndexWriter(files, os.path.join(self.out_dir, 'index.md'), root = self.out_dir)
        return w.write()



