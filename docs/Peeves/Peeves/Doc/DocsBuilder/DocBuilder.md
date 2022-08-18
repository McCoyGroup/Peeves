## <a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder">DocBuilder</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L10)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L10?message=Update%20Docs)]
</div>

A documentation builder class that uses a `DocWalker`
to build documentation, but which also has support for more
involved use cases, like setting up a `_config.yml` or other
documentation template things.



<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
 
### <a class="collapse-link" data-toggle="collapse" href="#methods">Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>

 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="methods" markdown="1">

```python
defaults_root: str
default_templates_extension: str
default_repo_templates_extension: str
default_config_file: str
config_defaults: dict
```
<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, packages=None, config=None, target=None, root=None, config_file=None, templates_directory=None, examples_directory=None, tests_directory=None, readme=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L23)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L23?message=Update%20Docs)]
</div>


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
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L73)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L73?message=Update%20Docs)]
</div>

Loads the config file to be used and fills in template parameters
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.create_layout" class="docs-object-method">&nbsp;</a> 
```python
create_layout(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L97)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L97?message=Update%20Docs)]
</div>

Creates the documentation layout that will be expanded upon by
a `DocWalker`
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.load_walker" class="docs-object-method">&nbsp;</a> 
```python
load_walker(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L133)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L133?message=Update%20Docs)]
</div>

Loads the `DocWalker` used to write docs.
A hook that can be overriden to sub in different walkers.
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.build" class="docs-object-method">&nbsp;</a> 
```python
build(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/DocsBuilder.py#L150)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L150?message=Update%20Docs)]
</div>

Writes documentation layout to `self.target`
- `:returns`: `_`
    >

 </div>
</div>



<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#tests">Tests</a> <a class="float-right" data-toggle="collapse" href="#tests"><i class="fa fa-chevron-down"></i></a>
 </div>
<div class="collapsible-section collapsible-section-body collapse show" id="tests" markdown="1">

- [PeevesDoc](#PeevesDoc)

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

 </div>
</div>

___

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/DocsBuilder/DocBuilder.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/DocsBuilder/DocBuilder.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/DocsBuilder/DocBuilder.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/DocsBuilder/DocBuilder.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/DocsBuilder.py#L10?message=Update%20Docs)