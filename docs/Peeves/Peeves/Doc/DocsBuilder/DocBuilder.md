## <a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder">DocBuilder</a>
A documentation builder class that uses a `DocWalker`
to build documentation, but which also has support for more
involved use cases, like setting up a `_config.yml` or other
documentation template things.



### Properties and Methods
```python
defaults_root: str
default_templates_extension: str
default_config_file: str
config_defaults: dict
```
<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, packages=None, config=None, target=None, root=None, config_file=None, templates_directory=None, examples_directory=None, tests_directory=None, readme=None): 
```

- `root`: `str`
    >root directory
root directory
- `target`: `str`
    >target directory to which files should be written
- `config`: `dict`
    >parameters for _config.yml file
- `packages`: `Iterable[str|dict]`
    >list of package configs to write

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.load_config" class="docs-object-method">&nbsp;</a>
```python
load_config(self): 
```
Loads the config file to be used and fills in template parameters
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.create_layout" class="docs-object-method">&nbsp;</a>
```python
create_layout(self): 
```
Creates the documentation layout that will be expanded upon by
a `DocWalker`
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.load_walker" class="docs-object-method">&nbsp;</a>
```python
load_walker(self): 
```
Loads the `DocWalker` used to write docs.
A hook that can be overriden to sub in different walkers.
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.build" class="docs-object-method">&nbsp;</a>
```python
build(self): 
```
Writes documentation layout to `self.target`
- `:returns`: `_`
    >



### Tests
- [PeevesDoc](#PeevesDoc)

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