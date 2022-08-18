## <a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter">TestExamplesFormatter</a>




### Properties and Methods
```python
default_template: str
default_example_template: str
```
<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, parser, template=None, example_template=None): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.from_file" class="docs-object-method">&nbsp;</a>
```python
from_file(tests_file): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format" class="docs-object-method">&nbsp;</a>
```python
format(self): 
```
Formats an examples file
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format_jump_links" class="docs-object-method">&nbsp;</a>
```python
format_jump_links(self, functions): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.TestExamplesFormatter.format_examples" class="docs-object-method">&nbsp;</a>
```python
format_examples(self): 
```



### Tests
- [ParseExamples](#ParseExamples)

#### Setup
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
#### <a name="ParseExamples">ParseExamples</a>
```python
    def test_ParseExamples(self):
        parser = ExamplesParser.from_file(os.path.abspath(__file__))
        self.assertTrue(hasattr(parser.functions, 'items'))
        tests = TestExamplesFormatter.from_file(os.path.abspath(__file__))
        print(tests.format())
```