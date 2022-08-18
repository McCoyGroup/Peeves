## <a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter">TestExamplesFormatter</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L207)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L207?message=Update%20Docs)]
</div>





<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
 
### <a class="collapse-link" data-toggle="collapse" href="#methods">Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>

 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="methods" markdown="1">

```python
default_template: str
default_example_template: str
```
<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, parser, template=None, example_template=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L208)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L208?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.from_file" class="docs-object-method">&nbsp;</a> 
```python
from_file(tests_file): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L214)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L214?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format" class="docs-object-method">&nbsp;</a> 
```python
format(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L237)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L237?message=Update%20Docs)]
</div>

Formats an examples file
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format_jump_links" class="docs-object-method">&nbsp;</a> 
```python
format_jump_links(self, functions): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L268)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L268?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format_examples" class="docs-object-method">&nbsp;</a> 
```python
format_examples(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/ExamplesParser.py#L279)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L279?message=Update%20Docs)]
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

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/ExamplesParser/TestExamplesFormatter.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/ExamplesParser/TestExamplesFormatter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/ExamplesParser/TestExamplesFormatter.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/ExamplesParser/TestExamplesFormatter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/ExamplesParser.py#L207?message=Update%20Docs)