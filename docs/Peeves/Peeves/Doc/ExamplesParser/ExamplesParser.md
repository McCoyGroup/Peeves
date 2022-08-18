## <a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser">ExamplesParser</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L9)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L9?message=Update%20Docs)]
</div>

Provides a parser for unit tests to turn them into examples

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
 
### <a class="collapse-link" data-toggle="collapse" href="#methods">Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>

 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="methods" markdown="1">

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, unit_tests): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L14)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L14?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.find_setup" class="docs-object-method">&nbsp;</a> 
```python
find_setup(self, tree_iter): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L23)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L23?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.parse_tests" class="docs-object-method">&nbsp;</a> 
```python
parse_tests(self, tree_iter): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L35)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L35?message=Update%20Docs)]
</div>

Parses out the
- `:returns`: `_`
    >
- `tree_iter`: `Any`
    >

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.walk_tree" class="docs-object-method">&nbsp;</a> 
```python
walk_tree(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L63)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L63?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.format_node" class="docs-object-method">&nbsp;</a> 
```python
format_node(self, node): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L77)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L77?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.from_file" class="docs-object-method">&nbsp;</a> 
```python
from_file(tests_file): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L87)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L87?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.class_spec" class="docs-object-method">&nbsp;</a> 
```python
@property
class_spec(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.setup" class="docs-object-method">&nbsp;</a> 
```python
@property
setup(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.functions" class="docs-object-method">&nbsp;</a> 
```python
@property
functions(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.functions_map" class="docs-object-method">&nbsp;</a> 
```python
@property
functions_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.load_function_map" class="docs-object-method">&nbsp;</a> 
```python
load_function_map(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L113)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L113?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.get_examples_functions" class="docs-object-method">&nbsp;</a> 
```python
get_examples_functions(self, node): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L180)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L180?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.filter_by_name" class="docs-object-method">&nbsp;</a> 
```python
filter_by_name(self, name): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L189)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L189?message=Update%20Docs)]
</div>

 </div>
</div>





<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#tests">Tests</a> <a class="float-right" data-toggle="collapse" href="#tests"><i class="fa fa-chevron-down"></i></a>
 </div>
<div class="collapsible-section collapsible-section-body collapse show" id="tests" markdown="1">

- [ParseExamples](#ParseExamples)

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
#### <a class="collapse-link" data-toggle="collapse" href="#test-setup">Setup</a> <a class="float-right" data-toggle="collapse" href="#test-setup"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="test-setup" markdown="1">

Before we can run our examples we should get a bit of setup out of the way.
Since these examples were harvested from the unit tests not all pieces
will be necessary for all situations.
```python
from Peeves.TestUtils import *
from unittest import TestCase
from Peeves.Doc import *
import os
```

All tests are wrapped in a test class
```python
class DocsTests(TestCase):
    """
    Sample documentation generator tests
    """
```

 </div>
</div>

#### <a name="ParseExamples">ParseExamples</a>
```python
    def test_ParseExamples(self):
        parser = ExamplesParser.from_file(os.path.abspath(__file__))
        self.assertTrue(hasattr(parser.functions, 'items'))
        tests = TestExamplesFormatter.from_file(os.path.abspath(__file__))
        print(tests.format())
```

 </div>
</div>

___

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/ExamplesParser/ExamplesParser.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/ExamplesParser/ExamplesParser.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/ExamplesParser/ExamplesParser.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/ExamplesParser/ExamplesParser.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L9?message=Update%20Docs)