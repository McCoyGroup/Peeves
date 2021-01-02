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

- `packages`: `Iterable[str|dict]`
    >list of package configs to write
- `config`: `dict`
    >parameters for _config.yml file
- `target`: `str`
    >target directory to which files should be written
- `root`: `str`
    >root directory

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.load_config" class="docs-object-method">&nbsp;</a>
```python
load_config(self): 
```
Loads the config file to be used and fills in template parameters
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.create_layout" class="docs-object-method">&nbsp;</a>
```python
create_layout(self): 
```
Creates the documentation layout that will be expanded upon by
        a `DocWalker`
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.load_walker" class="docs-object-method">&nbsp;</a>
```python
load_walker(self): 
```
Loads the `DocWalker` used to write docs.
        A hook that can be overriden to sub in different walkers.
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.DocsBuilder.DocBuilder.build" class="docs-object-method">&nbsp;</a>
```python
build(self): 
```
Writes documentation layout to `self.target`
- `:returns`: `_`
    >No description...

### Examples


