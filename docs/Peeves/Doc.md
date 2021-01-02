# <a id="Peeves.Doc">Peeves.Doc</a>
    
A file that only exists to make this directory useable as a way to import Peeves too.
Mostly useful during development

### Members:

  - [DocBuilder](Peeves/Doc/DocsBuilder/DocBuilder.md)
  - [DocWalker](Peeves/Doc/DocWalker/DocWalker.md)
  - [DocWriter](Peeves/Doc/Writers/DocWriter.md)
  - [ModuleWriter](Peeves/Doc/Writers/ModuleWriter.md)
  - [ClassWriter](Peeves/Doc/Writers/ClassWriter.md)
  - [FunctionWriter](Peeves/Doc/Writers/FunctionWriter.md)
  - [ObjectWriter](Peeves/Doc/Writers/ObjectWriter.md)
  - [IndexWriter](Peeves/Doc/Writers/IndexWriter.md)

### Examples:



```python

from Peeves.TestUtils import *
from unittest import TestCase
from Peeves.Doc import *

class DocsTests(TestCase):
    """
    Sample documentation generator tests
    """

    @debugTest
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
            "target": target
        }
        DocBuilder(**doc_config).build()
```