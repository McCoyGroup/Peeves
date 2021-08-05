## <a id="Peeves.Peeves.Doc.DocWalker.DocWalker">DocWalker</a>
A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
and a Markdown index file.

Takes a set of objects & writers and walks through the objects, generating files on the way

### Properties and Methods
```python
default_writers: OrderedDict
default_docs_ext: str
```
<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, objects, tree=None, out=None, docs_ext=None, writers=None, ignore_paths=None, description=None, verbose=True, extra_fields=None): 
```

- `objects`: `Iterable[Any]`
    >the objects to write out
- `out`: `None | str`
    >the directory in which to write the files (`None` means `sys.stdout`)
- ``: `DispatchTable`
    >writers
- `ignore_paths`: `None | Iterable[str]`
    >a set of paths not to write (passed to the objects)

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.resolve_spec" class="docs-object-method">&nbsp;</a>
```python
resolve_spec(self, spec, *args, **kwargs): 
```
Resolves an object spec.
- `spec`: `DocSpec`
    >object spec
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.write_object" class="docs-object-method">&nbsp;</a>
```python
write_object(self, o, parent=None): 
```
Writes a single object to file.
        Provides type dispatching to a writer, basically.
- `o`: `Any`
    >the object we want to write
- `parent`: `DocWriter`
    >the writer that was called right before this
- `:returns`: `None | str`
    >the written file

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.write_docs" class="docs-object-method">&nbsp;</a>
```python
write_docs(self): 
```
Walks through the objects supplied and writes them & their children to file
- `:returns`: `list[str]`
    >written files

### Examples


