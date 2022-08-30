## <a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter">TemplateFormatter</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine.py#L?message=Update%20Docs)]
</div>

Provides a formatter for fields that allows for
the inclusion of standard Bootstrap HTML elements
alongside the classic formatting







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="methods" markdown="1">
 ```python
max_recusion: <class 'int'>
directives: TemplateFormatDirective
frozendict: frozendict
```
<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, templates): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.format_parameters" class="docs-object-method">&nbsp;</a> 
```python
@property
format_parameters(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.templates" class="docs-object-method">&nbsp;</a> 
```python
@property
templates(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.special_callbacks" class="docs-object-method">&nbsp;</a> 
```python
@property
special_callbacks(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.callback_map" class="docs-object-method">&nbsp;</a> 
```python
@property
callback_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_eval_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_eval_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_directive_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_assignment" class="docs-object-method">&nbsp;</a> 
```python
apply_assignment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_raw" class="docs-object-method">&nbsp;</a> 
```python
apply_raw(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_comment" class="docs-object-method">&nbsp;</a> 
```python
apply_comment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive" class="docs-object-method">&nbsp;</a> 
```python
apply_directive(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.format_field" class="docs-object-method">&nbsp;</a> 
```python
format_field(self, value: Any, format_spec: str) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.load_template" class="docs-object-method">&nbsp;</a> 
```python
load_template(self, template): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateFormatter.vformat" class="docs-object-method">&nbsp;</a> 
```python
vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L?message=Update%20Docs)]
</div>
 </div>
</div>











---

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/TemplateEngine/TemplateFormatter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine.py#L?message=Update%20Docs)