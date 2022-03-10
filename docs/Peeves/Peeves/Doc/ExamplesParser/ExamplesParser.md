## <a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser">ExamplesParser</a>
Provides a parser for unit tests to turn them into examples

### Properties and Methods
<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, unit_tests): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.find_setup" class="docs-object-method">&nbsp;</a>
```python
find_setup(self, tree_iter): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.parse_tests" class="docs-object-method">&nbsp;</a>
```python
parse_tests(self, tree_iter): 
```
Parses out the
- `tree_iter`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.walk_tree" class="docs-object-method">&nbsp;</a>
```python
walk_tree(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.format_node" class="docs-object-method">&nbsp;</a>
```python
format_node(self, node): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.from_file" class="docs-object-method">&nbsp;</a>
```python
from_file(tests_file): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.class_spec" class="docs-object-method">&nbsp;</a>
```python
@property
class_spec(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.setup" class="docs-object-method">&nbsp;</a>
```python
@property
setup(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.functions" class="docs-object-method">&nbsp;</a>
```python
@property
functions(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.functions_map" class="docs-object-method">&nbsp;</a>
```python
@property
functions_map(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.load_function_map" class="docs-object-method">&nbsp;</a>
```python
load_function_map(self): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.get_examples_functions" class="docs-object-method">&nbsp;</a>
```python
get_examples_functions(self, node): 
```

<a id="Peeves.Peeves.Doc.ExamplesParser.ExamplesParser.filter_by_name" class="docs-object-method">&nbsp;</a>
```python
filter_by_name(self, name): 
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