## <a id="Peeves.Doc.ExamplesParser.ExamplesParser">ExamplesParser</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser.py#L8)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser.py#L8?message=Update%20Docs)]
</div>

Provides a parser for unit tests to turn them into examples







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 
<a id="Peeves.Doc.ExamplesParser.ExamplesParser.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, unit_tests): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L13)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L13?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.find_setup" class="docs-object-method">&nbsp;</a> 
```python
find_setup(self, tree_iter): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L22)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L22?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.parse_tests" class="docs-object-method">&nbsp;</a> 
```python
parse_tests(self, tree_iter): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L34)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L34?message=Update%20Docs)]
</div>
Parses out the
  - `tree_iter`: `Any`
    > 
  - `:returns`: `_`
    >


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.walk_tree" class="docs-object-method">&nbsp;</a> 
```python
walk_tree(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L62)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L62?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.format_node" class="docs-object-method">&nbsp;</a> 
```python
format_node(self, node): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L76)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L76?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.from_file" class="docs-object-method">&nbsp;</a> 
```python
from_file(tests_file): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L86)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L86?message=Update%20Docs)]
</div>


<a id="str.class_spec" class="docs-object-method">&nbsp;</a> 
```python
@property
class_spec(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/class_spec.py#L91)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/class_spec.py#L91?message=Update%20Docs)]
</div>


<a id="str.setup" class="docs-object-method">&nbsp;</a> 
```python
@property
setup(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/setup.py#L96)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/setup.py#L96?message=Update%20Docs)]
</div>


<a id="str.functions" class="docs-object-method">&nbsp;</a> 
```python
@property
functions(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/functions.py#L101)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/functions.py#L101?message=Update%20Docs)]
</div>


<a id="str.functions_map" class="docs-object-method">&nbsp;</a> 
```python
@property
functions_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/functions_map.py#L106)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/functions_map.py#L106?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.load_function_map" class="docs-object-method">&nbsp;</a> 
```python
load_function_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L112)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L112?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.get_examples_functions" class="docs-object-method">&nbsp;</a> 
```python
get_examples_functions(self, node): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L179)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L179?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.ExamplesParser.ExamplesParser.filter_by_name" class="docs-object-method">&nbsp;</a> 
```python
filter_by_name(self, name): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L188)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser/ExamplesParser.py#L188?message=Update%20Docs)]
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
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/ExamplesParser/ExamplesParser.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/ExamplesParser/ExamplesParser.md)   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/ExamplesParser/ExamplesParser.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/ExamplesParser/ExamplesParser.md)   
&lt;/div&gt;
   &lt;div class="col" markdown="1"&gt;
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/ExamplesParser.py#L8?message=Update%20Docs)   
&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
</div>