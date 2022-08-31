## <a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler">TemplateHandler</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L636)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L636?message=Update%20Docs)]
</div>









<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 ```python
template: NoneType
extension: str
squash_repeat_packages: bool
blacklist_packages: set
```
<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, obj, *, out=None, engine: Peeves.Peeves.Doc.TemplateEngine.TemplateEngine = None, root=None, squash_repeat_packages=True, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/__init__/__init__.py#L640)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/__init__/__init__.py#L640?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.template_params" class="docs-object-method">&nbsp;</a> 
```python
template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/template_params/__init__.py#L663)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/template_params/__init__.py#L663?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.get_template_params" class="docs-object-method">&nbsp;</a> 
```python
get_template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_template_params/__init__.py#L667)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_template_params/__init__.py#L667?message=Update%20Docs)]
</div>
Returns the parameters that should be inserted into the template
  - `:returns`: `dict`
    >


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.package_path" class="docs-object-method">&nbsp;</a> 
```python
@property
package_path(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/package_path/__init__.py#L677)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/package_path/__init__.py#L677?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.get_package_and_url" class="docs-object-method">&nbsp;</a> 
```python
get_package_and_url(self, include_url_base=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_package_and_url/__init__.py#L680)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_package_and_url/__init__.py#L680?message=Update%20Docs)]
</div>
Returns package name and corresponding URL for the object
being documented
  - `:returns`: `_`
    >


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.get_target_extension" class="docs-object-method">&nbsp;</a> 
```python
get_target_extension(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_target_extension/__init__.py#L716)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_target_extension/__init__.py#L716?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.get_output_file" class="docs-object-method">&nbsp;</a> 
```python
get_output_file(self, out): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_output_file/__init__.py#L726)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/get_output_file/__init__.py#L726?message=Update%20Docs)]
</div>
Returns package name and corresponding URL for the object
being documented
  - `:returns`: `_`
    >


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.handle" class="docs-object-method">&nbsp;</a> 
```python
handle(self, template=None, target=None, write=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/handle/__init__.py#L746)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/handle/__init__.py#L746?message=Update%20Docs)]
</div>
Formats the documentation Markdown from the supplied template
  - `template`: `Any`
    > 
  - `:returns`: `_`
    >


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateHandler.check_should_write" class="docs-object-method">&nbsp;</a> 
```python
check_should_write(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/check_should_write/__init__.py#L814)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/check_should_write/__init__.py#L814?message=Update%20Docs)]
</div>
Determines whether the object really actually should be
documented (quite permissive)
  - `:returns`: `_`
    >
 </div>
</div>











---


<div markdown="1" class="text-secondary">
<div class="container">
  <div class="row">
   <div class="col" markdown="1">
**Feedback**   
</div>
   <div class="col" markdown="1">
**Examples**   
</div>
   <div class="col" markdown="1">
**Templates**   
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
[Bug](https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)/[Request](https://github.com/McCoyGroup/Peeves/issues/new?title=Example%20Request)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/TemplateHandler.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/TemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/TemplateHandler.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/TemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateHandler/__init__.py#L636?message=Update%20Docs)   
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