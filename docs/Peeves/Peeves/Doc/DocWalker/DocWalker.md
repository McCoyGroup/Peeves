## <a id="Peeves.Peeves.Doc.DocWalker.DocWalker">DocWalker</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocWalker.py#L124)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L124?message=Update%20Docs)]
</div>

A class that walks a module structure, generating .md files for every class inside it as well as for global functions,
and a Markdown index file.

Takes a set of objects & writers and walks through the objects, generating files on the way

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
 
### <a class="collapse-link" data-toggle="collapse" href="#methods">Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>

 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="methods" markdown="1">

```python
default_writers: OrderedDict
default_docs_ext: str
```
<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, objects, tree=None, out=None, docs_ext=None, writers=None, ignore_paths=None, description=None, verbose=True, template_directory=None, examples_directory=None, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocWalker.py#L138)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L138?message=Update%20Docs)]
</div>


- `ignore_paths`: `None | Iterable[str]`
    >a set of paths not to write (passed to the objects)
- ``: `DispatchTable`
    >writers
- `out`: `None | str`
    >the directory in which to write the files (`None` means `sys.stdout`)
the directory in which to write the files (`None` means `sys.stdout`)
- `objects`: `Iterable[Any]`
    >the objects to write out

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.resolve_spec" class="docs-object-method">&nbsp;</a> 
```python
resolve_spec(self, spec, *args, template_directory=None, examples_directory=None, extra_fields=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocWalker.py#L216)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L216?message=Update%20Docs)]
</div>

Resolves an object spec.
- `:returns`: `_`
    >
- `spec`: `DocSpec`
    >object spec

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.write_object" class="docs-object-method">&nbsp;</a> 
```python
write_object(self, o, parent=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocWalker.py#L248)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L248?message=Update%20Docs)]
</div>

Writes a single object to file.
Provides type dispatching to a writer, basically.
- `:returns`: `None | str`
    >t
h
e
 
w
r
i
t
t
e
n
 
f
i
l
e
- `parent`: `DocWriter`
    >the writer that was called right before this
- `o`: `Any`
    >the object we want to write

<a id="Peeves.Peeves.Doc.DocWalker.DocWalker.write_docs" class="docs-object-method">&nbsp;</a> 
```python
write_docs(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocWalker.py#L300)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L300?message=Update%20Docs)]
</div>

Walks through the objects supplied and writes them & their children to file
- `:returns`: `list[str]`
    >w
r
i
t
t
e
n
 
f
i
l
e
s

 </div>
</div>






___

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/DocWalker/DocWalker.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/DocWalker/DocWalker.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/DocWalker/DocWalker.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/DocWalker/DocWalker.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocWalker.py#L124?message=Update%20Docs)