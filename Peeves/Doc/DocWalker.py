"""
Provides a class that will walk through a set of objects & their children, as loaded into memory, and will generate Markdown for each.
The actual object Markdown is written by the things in the `Writers` module.
"""

import os, types, collections
from .TemplateEngine import TemplateWalker
from .ObjectWalker import ObjectSpec
from .Writers import *

__all__ = [ "DocWalker" ]

class DocSpec(ObjectSpec):
    """
    A specification for an object to document.
    Supports the fields given by `spec_fields`.
    """
    spec_fields = (
        'id', # name for resolving the object
        'parent', # parent object name for writing,
        'children',
        'examples_root',
        'tests_root'
    )

    def __repr__(self):
        return '{}({})'.format(
            type(self).__name__,
            super().__repr__()
        )

class DocWalker(TemplateWalker):
    """
    A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
    and a Markdown index file.

    Takes a set of objects & writers and walks through the objects, generating files on the way
    """

    default_handlers = collections.OrderedDict((
        ((str, types.ModuleType), ModuleWriter),
        ((type,), ClassWriter),
        ((types.FunctionType,), FunctionWriter)
    ))
    default_docs_ext='Documentation'
    def __init__(self,
                 objects,
                 out=None,
                 docs_ext=None,
                 writers=None,
                 ignore_paths=None,
                 description=None,
                 verbose=True,
                 template_directory=None,
                 examples_directory=None,
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

        self.objects = objects
        super().__init__(handlers=writers, **extra_fields)

        self.template_directory = template_directory
        self.examples_directory = examples_directory

        self.ignore_paths = ignore_paths

        if out is None:
            if docs_ext is None:
                docs_ext = self.default_docs_ext
            out = os.path.join(os.getcwd(), docs_ext)
        self.out_dir = out
        try:
            os.makedirs(self.out_dir)
        except OSError:
            pass

        self.description = description
        self.verbose = verbose

    @property
    def _initial_writers(self):
        """
        Adds a minor hook onto the default_writes dict and returns it
        :return:
        :rtype:
        """

        writers = self.default_writers.copy()
        writers[DocSpec] = self.resolve_spec
        return writers

    def resolve_spec(self, spec, *args,
                     template_directory=None,
                     examples_directory=None,
                     extra_fields=None,
                     **kwargs
                     ):
        """
        Resolves an object spec.

        :param spec: object spec
        :type spec: DocSpec
        :return:
        :rtype:
        """

        # for the moment we only reolve using the `id` parameter
        oid = spec['id']
        o = DocWriter.resolve_object(oid)
        # but we attach all of the other info

        template_directory = self.template_directory if template_directory is None else template_directory
        examples_directory = self.examples_directory if examples_directory is None else examples_directory
        extra_fields = self.extra_fields if extra_fields is None else extra_fields

        return self.writers(o, *args,
                            spec=spec,
                            template_directory=template_directory,
                            examples_directory=examples_directory,
                            extra_fields=extra_fields,
                            **kwargs
                            )

    def write_object(self, o, parent=None, **kwargs):
        """
        Writes a single object to file.
        Provides type dispatching to a writer, basically.

        :param o: the object we want to write
        :type o:
        :param parent: the writer that was called right before this
        :type parent: DocWriter
        :return: the written file
        :rtype: None | str
        """

        if (
                isinstance(o, (dict, collections.OrderedDict))
                and all(k in o for k in ['id'])
        ):
            o = DocSpec(o.items())

        if parent is not None:
            pid = parent.identifier
            ptests = parent.tests
        else:
            pid = None
            ptests = None

        writer = self.writers(o,
                              self.out_dir,
                              parent=pid,
                              parent_tests=ptests,
                              tree=self.tree,
                              ignore_paths=self.ignore_paths,
                              template_directory=self.template_directory,
                              examples_directory=self.examples_directory,
                              **dict(self.extra_fields, **kwargs)
                              )

        oid = writer.identifier
        if oid not in self.tree:
            res = writer.write()
            if res is not None: # basically means stop writing
                spec = writer.doc_spec
                spec.update(file=res)
                self.tree[oid] = spec

                for child in writer.children:
                    self.write_object(child,
                                      parent=writer,
                                      **dict(writer.extra_fields, **kwargs)
                                      )
            return res

    def write_docs(self):
        """
        Walks through the objects supplied and writes them & their children to file
        :return: written files
        :rtype: list[str]
        """

        if self.verbose:
            print("Generating documentation to {}".format(self.out_dir))
        files = [ self.write_object(o) for o in self.objects ]
        files = [ f for f in files if f is not None ]
        w = IndexWriter(files, os.path.join(self.out_dir, 'index.md'),
                        description=self.description,
                        root=self.out_dir,
                        template_directory=self.template_directory,
                        examples_directory=self.examples_directory,
                        extra_fields=self.extra_fields
                        )
        return w.write()



