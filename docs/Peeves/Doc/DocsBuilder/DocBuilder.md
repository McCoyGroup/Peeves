## <a id="Peeves.Doc.DocsBuilder.DocBuilder">DocBuilder</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder.py#L11)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder.py#L11?message=Update%20Docs)]
</div>

A documentation builder class that uses a `DocWalker`
to build documentation, but which also has support for more
involved use cases, like setting up a `_config.yml` or other
documentation template things.







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 ```python
defaults_root: str
default_config_file: str
default_template_extension: str
default_repo_extension: str
config_defaults: dict
```
<a id="Peeves.Doc.DocsBuilder.DocBuilder.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, packages=None, config=None, target=None, root=None, config_file=None, templates_directory=None, examples_directory=None, tests_directory=None, readme=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L26)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L26?message=Update%20Docs)]
</div>

  - `packages`: `Iterable[str|dict]`
    > list of package configs to write
  - `config`: `dict`
    > parameters for _config.yml file
  - `target`: `str`
    > target directory to which files should be written
  - `root`: `str`
    > root directory
root directory


<a id="Peeves.Doc.DocsBuilder.DocBuilder.get_template_locator" class="docs-object-method">&nbsp;</a> 
```python
get_template_locator(self, template_directory, use_repo_templates=False): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L66)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L66?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocsBuilder.DocBuilder.load_config" class="docs-object-method">&nbsp;</a> 
```python
load_config(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L87)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L87?message=Update%20Docs)]
</div>
Loads the config file to be used and fills in template parameters
  - `:returns`: `_`
    >


<a id="Peeves.Doc.DocsBuilder.DocBuilder.create_layout" class="docs-object-method">&nbsp;</a> 
```python
create_layout(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L111)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L111?message=Update%20Docs)]
</div>
Creates the documentation layout that will be expanded upon by
a `DocWalker`
  - `:returns`: `_`
    >


<a id="Peeves.Doc.DocsBuilder.DocBuilder.load_walker" class="docs-object-method">&nbsp;</a> 
```python
load_walker(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L145)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L145?message=Update%20Docs)]
</div>
Loads the `DocWalker` used to write docs.
A hook that can be overriden to sub in different walkers.
  - `:returns`: `_`
    >


<a id="Peeves.Doc.DocsBuilder.DocBuilder.build" class="docs-object-method">&nbsp;</a> 
```python
build(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L161)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder.py#L161?message=Update%20Docs)]
</div>
Writes documentation layout to `self.target`
  - `:returns`: `_`
    >
 </div>
</div>









<div markdown="1" class="alert alert-info">
**See Also:** [`DocWalker`](../DocWalker/DocWalker.md)<span>&nbsp;&#9642;&nbsp;</span>[`ModuleWriter`](../DocWalker/ModuleWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ClassWriter`](../DocWalker/ClassWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`FunctionWriter`](../DocWalker/FunctionWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`MethodWriter`](../DocWalker/MethodWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ObjectWriter`](../DocWalker/ObjectWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`IndexWriter`](../DocWalker/IndexWriter.md)
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
</div>
  <div class="row">
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/DocsBuilder/DocBuilder.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/DocsBuilder/DocBuilder.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/DocsBuilder/DocBuilder.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/DocsBuilder/DocBuilder.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder.py#L11?message=Update%20Docs)   
</div>
</div>
</div>
</div>