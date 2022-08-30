## <a id="Peeves.Doc.TemplateEngine.TemplateFormatter">TemplateFormatter</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/__init__.py#L?message=Update%20Docs)]
</div>

Provides a formatter for fields that allows for
the inclusion of standard Bootstrap HTML elements
alongside the classic formatting







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 ```python
max_recusion: int
directives: TemplateFormatDirective
frozendict: frozendict
```
<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, templates): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/__init__/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/__init__/__init__.py#L?message=Update%20Docs)]
</div>


<a id="str.format_parameters" class="docs-object-method">&nbsp;</a> 
```python
@property
format_parameters(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/format_parameters/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/format_parameters/__init__.py#L?message=Update%20Docs)]
</div>


<a id="str.templates" class="docs-object-method">&nbsp;</a> 
```python
@property
templates(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/templates/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/templates/__init__.py#L?message=Update%20Docs)]
</div>


<a id="str.special_callbacks" class="docs-object-method">&nbsp;</a> 
```python
@property
special_callbacks(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/special_callbacks/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/special_callbacks/__init__.py#L?message=Update%20Docs)]
</div>


<a id="str.callback_map" class="docs-object-method">&nbsp;</a> 
```python
@property
callback_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/callback_map/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/callback_map/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_eval_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_eval_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_eval_tree/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_eval_tree/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_directive_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_directive_tree/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_directive_tree/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_assignment" class="docs-object-method">&nbsp;</a> 
```python
apply_assignment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_assignment/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_assignment/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_raw" class="docs-object-method">&nbsp;</a> 
```python
apply_raw(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_raw/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_raw/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_comment" class="docs-object-method">&nbsp;</a> 
```python
apply_comment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_comment/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_comment/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive" class="docs-object-method">&nbsp;</a> 
```python
apply_directive(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_directive/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/apply_directive/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.format_field" class="docs-object-method">&nbsp;</a> 
```python
format_field(self, value: Any, format_spec: str) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/format_field/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/format_field/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.load_template" class="docs-object-method">&nbsp;</a> 
```python
load_template(self, template): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/load_template/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/load_template/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.vformat" class="docs-object-method">&nbsp;</a> 
```python
vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter/vformat/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/vformat/__init__.py#L?message=Update%20Docs)]
</div>
 </div>
</div>











---

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/TemplateEngine/TemplateFormatter.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/TemplateEngine/TemplateFormatter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/TemplateEngine/TemplateFormatter.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/TemplateEngine/TemplateFormatter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter/__init__.py#L?message=Update%20Docs)