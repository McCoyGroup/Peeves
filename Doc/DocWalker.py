"""
A class that walks a module structure, generating .md files for every class inside it as well as for global functions, \
and a Markdown index file
"""

from .Writers import *
import os

__all__ = [ "DocWalker" ]

class DocWalker:
    def __init__(self, objects, out = None,
                 module_writer = None, class_writer = None, function_writer = None, object_writer = None):
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

        if out is None:
            out = os.path.join(os.getcwd(), "docs")
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
                writer = self.class_writer(o, self.out_dir)
                res = writer.write()
                written.add(oid)
                return res
        elif isinstance(o, types.FunctionType):
            oid = self.function_writer.get_identifier(o)
            if not oid in written:
                writer = self.function_writer(o, self.out_dir)
                res = writer.write()
                written.add(oid)
                return res
        elif isinstance(o, types.ModuleType) or isinstance(o, str):
            if isinstance(o, str):
                try:
                    o = __import__(o)
                except ModuleNotFoundError: # tried to load a member but couldn't...
                    p_split = o.split(".")
                    mod_spec = ".".join(p_split[:-1])
                    mood = __import__(mod_spec)
                    from functools import reduce
                    v = reduce(lambda m,a: getattr(m, a), p_split[1:], mood)
                    return self.write_object(v, written)

            oid = self.module_writer.get_identifier(o)
            if not oid in written:
                writer = self.module_writer(o, self.out_dir)
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
                if hasattr(o, "__doc__"):
                    w = self.object_writer(o, self.out_dir)
                    oid = w.identifier
                    if not oid in written:
                        res = w.write()
                        written.add(oid)
                        return res

    def write_docs(self):
        files = [ self.write_object(o) for o in self.objects ]
        w = IndexWriter(files, os.path.join(self.out_dir, 'index.md'), root = self.out_dir)
        return w.write()



