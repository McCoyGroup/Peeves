# <a id="Peeves.Doc">Peeves.Doc</a>
    
Simple Documentation framework that takes all of the python docstrings and unwraps them into proper docs while supporting
example and template files

### Members:

<div class="container alert alert-secondary bg-light">
  <div class="row">
   <div class="col" markdown="1">
[DocBuilder](Peeves/Doc/DocsBuilder/DocBuilder.md)   
</div>
   <div class="col" markdown="1">
[DocWalker](Peeves/Doc/DocWalker/DocWalker.md)   
</div>
   <div class="col" markdown="1">
[DocWriter](Peeves/Doc/Writers/DocWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ModuleWriter](Peeves/Doc/Writers/ModuleWriter.md)   
</div>
   <div class="col" markdown="1">
[ClassWriter](Peeves/Doc/Writers/ClassWriter.md)   
</div>
   <div class="col" markdown="1">
[FunctionWriter](Peeves/Doc/Writers/FunctionWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ObjectWriter](Peeves/Doc/Writers/ObjectWriter.md)   
</div>
   <div class="col" markdown="1">
[IndexWriter](Peeves/Doc/Writers/IndexWriter.md)   
</div>
   <div class="col" markdown="1">
[ExamplesParser](Peeves/Doc/ExamplesParser/ExamplesParser.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TestExamplesFormatter](Peeves/Doc/ExamplesParser/TestExamplesFormatter.md)   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
</div>



### Tests
- [PeevesDoc](#PeevesDoc)
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
#### <a name="PeevesDoc">PeevesDoc</a>
```python
    def test_PeevesDoc(self):
        """
        Builds sample documentation for the Peeves package

        :return:
        :rtype:
        """

        import os

        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        target = os.path.expanduser("~/Desktop/docs")
        doc_config = {
            "config": {
                "theme": "McCoyGroup/finx",
                "title": "Peeves",
                "path": "",
                "url": "https://mccoygrp.github.io/Peeves/"
            },
            "packages": [
                {
                    "id": "Peeves",
                    'tests_root': os.path.join(root, "ci", "tests")
                }
            ],
            "root": root,
            "target": target,
            'readme': os.path.join(root, "README.md")
        }
        DocBuilder(**doc_config).build()
```
#### <a name="ParseExamples">ParseExamples</a>
```python
    def test_ParseExamples(self):
        parser = ExamplesParser.from_file(os.path.abspath(__file__))
        self.assertTrue(hasattr(parser.functions, 'items'))
        tests = TestExamplesFormatter.from_file(os.path.abspath(__file__))
        print(tests.format())
```