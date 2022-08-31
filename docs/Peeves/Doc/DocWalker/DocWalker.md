## <a id="Peeves.Doc.DocWalker.DocWalker">DocWalker</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker.py#L574)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker.py#L574?message=Update%20Docs)]
</div>

A class that walks a module structure, generating `.md` files for every class inside it as well as for global functions,
and a Markdown index file.

Takes a set of objects & writers and walks through the objects, generating files on the way.







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 ```python
module_handler: ModuleWriter
class_handler: ClassWriter
function_handler: FunctionWriter
method_handler: MethodWriter
object_handler: ObjectWriter
index_handler: IndexWriter
spec: DocSpec
```
<a id="Peeves.Doc.DocWalker.DocWalker.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, out=None, engine=None, verbose=True, template_locator=None, examples_directory=None, tests_directory=None, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L592)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L592?message=Update%20Docs)]
</div>

  - `objects`: `Iterable[Any]`
    > the objects to write out
  - `out`: `None | str`
    > the directory in which to write the files (`None` means `sys.stdout`)
the directory in which to write the files (`None` means `sys.stdout`)
  - ``: `DispatchTable`
    > writers
  - `ignore_paths`: `None | Iterable[str]`
    > a set of paths not to write (passed to the objects)


<a id="Peeves.Doc.DocWalker.DocWalker.get_engine" class="docs-object-method">&nbsp;</a> 
```python
get_engine(self, locator): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L622)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L622?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocWalker.DocWalker.get_examples_loader" class="docs-object-method">&nbsp;</a> 
```python
get_examples_loader(self, examples_directory): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L626)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L626?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocWalker.DocWalker.get_tests_loader" class="docs-object-method">&nbsp;</a> 
```python
get_tests_loader(self, tests_directory): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L631)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L631?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocWalker.DocWalker.get_handler" class="docs-object-method">&nbsp;</a> 
```python
get_handler(self, *args, examples_loader=None, tests_loader=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L636)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L636?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocWalker.DocWalker.visit_root" class="docs-object-method">&nbsp;</a> 
```python
visit_root(self, o, tests_directory=None, examples_directory=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocWalker/DocWalker.py#L644)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker/DocWalker.py#L644?message=Update%20Docs)]
</div>
 </div>
</div>



<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#Details-e5db8b" markdown="1"> Details</a> <a class="float-right" data-toggle="collapse" href="#Details-e5db8b"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="Details-e5db8b" markdown="1">
 A `DocWalker` object is a light subclass of a `TemplateWalker`, but specialized for documentation & with specialized handlers
 </div>
</div>







<div markdown="1" class="alert alert-info">
**See Also:** [`DocBuilder`](../DocsBuilder/DocBuilder.md)<span>&nbsp;&#9642;&nbsp;</span>[`ModuleWriter`](ModuleWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ClassWriter`](ClassWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`FunctionWriter`](FunctionWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`MethodWriter`](MethodWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ObjectWriter`](ObjectWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`IndexWriter`](IndexWriter.md)
</div>

---


<div markdown="1" class="text-secondary fs-3">
<div class="container">
  <div class="row">
   <div class="col" markdown="1">
[Give Feedback](https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
**Examples**   
</div>
   <div class="col" markdown="1">
**Template**   
</div>
   <div class="col" markdown="1">
**Documentation**   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/DocWalker/DocWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/DocWalker/DocWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/DocWalker/DocWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/DocWalker/DocWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocWalker.py#L574?message=Update%20Docs)   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
</div>
</div>