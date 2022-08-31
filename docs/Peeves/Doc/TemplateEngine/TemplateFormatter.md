## <a id="Peeves.Doc.TemplateEngine.TemplateFormatter">TemplateFormatter</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine.py#L349)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine.py#L349?message=Update%20Docs)]
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
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L360)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L360?message=Update%20Docs)]
</div>


<a id="str.format_parameters" class="docs-object-method">&nbsp;</a> 
```python
@property
format_parameters(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/format_parameters.py#L363)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/format_parameters.py#L363?message=Update%20Docs)]
</div>


<a id="str.templates" class="docs-object-method">&nbsp;</a> 
```python
@property
templates(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/templates.py#L366)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/templates.py#L366?message=Update%20Docs)]
</div>


<a id="str.special_callbacks" class="docs-object-method">&nbsp;</a> 
```python
@property
special_callbacks(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/special_callbacks.py#L369)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/special_callbacks.py#L369?message=Update%20Docs)]
</div>


<a id="str.callback_map" class="docs-object-method">&nbsp;</a> 
```python
@property
callback_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/callback_map.py#L372)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/callback_map.py#L372?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_eval_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_eval_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L379)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L379?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive_tree" class="docs-object-method">&nbsp;</a> 
```python
apply_directive_tree(self, _, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L385)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L385?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_assignment" class="docs-object-method">&nbsp;</a> 
```python
apply_assignment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L387)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L387?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_raw" class="docs-object-method">&nbsp;</a> 
```python
apply_raw(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L391)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L391?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_comment" class="docs-object-method">&nbsp;</a> 
```python
apply_comment(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L393)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L393?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.apply_directive" class="docs-object-method">&nbsp;</a> 
```python
apply_directive(self, key, spec) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L395)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L395?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.format_field" class="docs-object-method">&nbsp;</a> 
```python
format_field(self, value: Any, format_spec: str) -> str: 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L400)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L400?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.load_template" class="docs-object-method">&nbsp;</a> 
```python
load_template(self, template): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L417)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L417?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateFormatter.vformat" class="docs-object-method">&nbsp;</a> 
```python
vformat(self, format_string: str, args: Sequence[Any], kwargs: Mapping[str, Any]): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L441)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateFormatter.py#L441?message=Update%20Docs)]
</div>
 </div>
</div>











---


<div markdown="1" class="text-muted">
&lt;div class="container"&gt;
  &lt;div class="row"&gt;
   &lt;div class="col" markdown="1"&gt;
[Feedback](https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)   
&lt;/div&gt;
&lt;/div&gt;
  &lt;div class="row"&gt;
   &lt;div class="col" markdown="1"&gt;
Examples   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
Template   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
Documentation   
&lt;/div&gt;
&lt;/div&gt;
  &lt;div class="row"&gt;
   &lt;div class="col" markdown="1"&gt;
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/TemplateEngine/TemplateFormatter.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/TemplateEngine/TemplateFormatter.md)   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/TemplateEngine/TemplateFormatter.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/TemplateEngine/TemplateFormatter.md)   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine.py#L349?message=Update%20Docs)   
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
</div>