# <a id="Peeves.Doc">Peeves.Doc</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/tree/master/Peeves/Doc)]
</div>
    
Simple Documentation framework that takes all of the python docstrings and unwraps them into proper docs while supporting
example and template files

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






<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#tests">Tests</a> <a class="float-right" data-toggle="collapse" href="#tests"><i class="fa fa-chevron-down"></i></a>
 </div>
<div class="collapsible-section collapsible-section-body collapse show" id="tests" markdown="1">

- [PeevesDoc](#PeevesDoc)
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

 </div>
</div>

___

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/master/ci/examples/Peeves/Doc.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/master/?filename=ci/examples/Peeves/Doc.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/master/ci/docs/Peeves/Doc.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/master/?filename=ci/docs/templates/Peeves/Doc.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py?message=Update%20Docs)