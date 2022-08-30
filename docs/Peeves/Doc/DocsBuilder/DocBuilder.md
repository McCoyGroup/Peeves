## <a id="Peeves.Doc.DocsBuilder.DocBuilder">DocBuilder</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/__init__.py#L?message=Update%20Docs)]
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
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/__init__/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/__init__/__init__.py#L?message=Update%20Docs)]
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
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/get_template_locator/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/get_template_locator/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.DocsBuilder.DocBuilder.load_config" class="docs-object-method">&nbsp;</a> 
```python
load_config(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/load_config/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/load_config/__init__.py#L?message=Update%20Docs)]
</div>
Loads the config file to be used and fills in template parameters
  - `:returns`: `_`
    >


<a id="Peeves.Doc.DocsBuilder.DocBuilder.create_layout" class="docs-object-method">&nbsp;</a> 
```python
create_layout(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/create_layout/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/create_layout/__init__.py#L?message=Update%20Docs)]
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
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/load_walker/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/load_walker/__init__.py#L?message=Update%20Docs)]
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
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/DocsBuilder/DocBuilder/build/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/build/__init__.py#L?message=Update%20Docs)]
</div>
Writes documentation layout to `self.target`
  - `:returns`: `_`
    >
 </div>
</div>









**See Also:** [`DocWalker`](../DocWalker/DocWalker.md)<span>&nbsp;&#9642;&nbsp;</span>[`ModuleWriter`](../DocWalker/ModuleWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ClassWriter`](../DocWalker/ClassWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`FunctionWriter`](../DocWalker/FunctionWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`MethodWriter`](../DocWalker/MethodWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`ObjectWriter`](../DocWalker/ObjectWriter.md)<span>&nbsp;&#9642;&nbsp;</span>[`IndexWriter`](../DocWalker/IndexWriter.md)

---

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/DocsBuilder/DocBuilder.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/DocsBuilder/DocBuilder.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/DocsBuilder/DocBuilder.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/DocsBuilder/DocBuilder.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/DocsBuilder/DocBuilder/__init__.py#L?message=Update%20Docs)