## <a id="Peeves.Doc.TemplateEngine.TemplateHandler">TemplateHandler</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L?message=Update%20Docs)]
</div>









<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="methods" markdown="1">
 ```python
template: NoneType
extension: str
squash_repeat_packages: bool
blacklist_packages: set
```
<a id="Peeves.Doc.TemplateEngine.TemplateHandler.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, obj, *, out=None, engine: Peeves.Peeves.Doc.TemplateEngine.TemplateEngine = None, root=None, squash_repeat_packages=True, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/__init__/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/__init__/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.template_params" class="docs-object-method">&nbsp;</a> 
```python
template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/template_params/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/template_params/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.get_template_params" class="docs-object-method">&nbsp;</a> 
```python
get_template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_template_params/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_template_params/__init__.py#L?message=Update%20Docs)]
</div>
Returns the parameters that should be inserted into the template
  - `:returns`: `dict`
    >


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.get_identifier" class="docs-object-method">&nbsp;</a> 
```python
get_identifier(o): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_identifier/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_identifier/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.get_package_and_url" class="docs-object-method">&nbsp;</a> 
```python
get_package_and_url(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_package_and_url/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/get_package_and_url/__init__.py#L?message=Update%20Docs)]
</div>
Returns package name and corresponding URL for the object
being documented
  - `:returns`: `_`
    >


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.handle" class="docs-object-method">&nbsp;</a> 
```python
handle(self, template=None, target=None, write=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/handle/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/handle/__init__.py#L?message=Update%20Docs)]
</div>
Formats the documentation Markdown from the supplied template
  - `template`: `Any`
    > 
  - `:returns`: `_`
    >


<a id="Peeves.Doc.TemplateEngine.TemplateHandler.check_should_write" class="docs-object-method">&nbsp;</a> 
```python
check_should_write(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateHandler/check_should_write/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/check_should_write/__init__.py#L?message=Update%20Docs)]
</div>
Determines whether the object really actually should be
documented (quite permissive)
  - `:returns`: `_`
    >
 </div>
</div>











---

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/TemplateEngine/TemplateHandler.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/TemplateEngine/TemplateHandler.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/TemplateEngine/TemplateHandler.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/TemplateEngine/TemplateHandler.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L?message=Update%20Docs)