## <a id="Peeves.Peeves.Doc.Writers.DocWriter">DocWriter</a>
A general writer class that writes a file based off a template and filling in object template specs

### Properties and Methods
```python
template: str
template_root: str
template_name: str
default_template_dir: str
default_examples_root: str
default_tests_root: str
outStream: type
blacklist_packages: set
load_template: method
get_identifier: method
param_template: str
```
<a id="Peeves.Peeves.Doc.Writers.DocWriter.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, obj, out_file, tree=None, name=None, parent=None, spec=None, template=None, root=None, ignore_paths=None, examples=None, tests=None, formatter=None): 
```

- `obj`: `Any`
    >object to write
- `out_file`: `str | None`
    >file to write to
- `tree`: `Any`
    >tree of written docs for looking stuff up
- `name`: `Any`
    >name to be used in the docs
- `parent`: `Any`
    >parent object for docs purposes
- `spec`: `dict | None`
    >extra parameters that are usually inherited from the parent writer
- `template`: `str | None`
    >template string to use when generating files
- `root`: `str | None`
    >root directory to build off of
- `ignore_paths`: `Iterable[str]`
    >paths to never write
- `examples`: `str | None`
    >path to examples to load
- `tests`: `str | None`
    >path to tests to load
- `formatter`: `Any`
    >object that can format the stuff that Markdown supports

<a id="Peeves.Peeves.Doc.Writers.DocWriter.name" class="docs-object-method">&nbsp;</a>
```python
@property
name(self): 
```
Returns the name (not full identifier) of the object
        being documented
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_name" class="docs-object-method">&nbsp;</a>
```python
get_name(self): 
```
Returns the name the object will have in its documentation page
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.out" class="docs-object-method">&nbsp;</a>
```python
@property
out(self): 
```

<a id="Peeves.Peeves.Doc.Writers.DocWriter.write_string" class="docs-object-method">&nbsp;</a>
```python
write_string(self, txt): 
```

<a id="Peeves.Peeves.Doc.Writers.DocWriter.template_params" class="docs-object-method">&nbsp;</a>
```python
template_params(self): 
```
Returns the parameters that should be inserted into the template
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.format" class="docs-object-method">&nbsp;</a>
```python
format(self, template=None): 
```
Formats the documentation Markdown from the supplied template
- `template`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.check_should_write" class="docs-object-method">&nbsp;</a>
```python
check_should_write(self): 
```
Determines whether the object really actually should be
        documented (quite permissive)
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.write" class="docs-object-method">&nbsp;</a>
```python
write(self, template=None): 
```
Writes the actual docs file
- `template`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_package_and_url" class="docs-object-method">&nbsp;</a>
```python
get_package_and_url(self): 
```
Returns package name and corresponding URL for the object
        being documented
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.package_path" class="docs-object-method">&nbsp;</a>
```python
@property
package_path(self): 
```

<a id="Peeves.Peeves.Doc.Writers.DocWriter.identifier" class="docs-object-method">&nbsp;</a>
```python
@property
identifier(self): 
```

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resource_dir" class="docs-object-method">&nbsp;</a>
```python
resource_dir(self, spec_key, base_root): 
```
Returns the directory for a given resource (e.g. examples or tests)
        by trying a number of different possible locations
- `spec_key`: `Any`
    >No description...
- `base_root`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.find_template" class="docs-object-method">&nbsp;</a>
```python
find_template(self, template): 
```
Finds the appropriate template for the object by looking
        in a variety of different locations
- `template`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.examples_dir" class="docs-object-method">&nbsp;</a>
```python
@property
examples_dir(self): 
```
Returns the directory in which to look for examples
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.examples_path" class="docs-object-method">&nbsp;</a>
```python
@property
examples_path(self): 
```
Provides the default examples path for the object
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.load_examples" class="docs-object-method">&nbsp;</a>
```python
load_examples(self): 
```
Loads examples for the stored object if provided
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.tests_dir" class="docs-object-method">&nbsp;</a>
```python
@property
tests_dir(self): 
```
Returns the directory in which to look for tests
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.tests_path" class="docs-object-method">&nbsp;</a>
```python
@property
tests_path(self): 
```
Provides the default tests path for the object
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.load_tests" class="docs-object-method">&nbsp;</a>
```python
load_tests(self): 
```
Loads examples for the stored object if provided
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.parent" class="docs-object-method">&nbsp;</a>
```python
@property
parent(self): 
```
Returns the parent object for docs purposes
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_parent" class="docs-object-method">&nbsp;</a>
```python
resolve_parent(self, check_tree=True): 
```
Resolves the "parent" of obj.
        By default, just the module in which it is contained.
        Allows for easy skipping of pieces of the object tree,
        though, since a parent can be directly added to the set of
        written object which is distinct from the module it would
        usually resolve to.
        Also can be subclassed to provide more fine grained behavior.
- `obj`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.children" class="docs-object-method">&nbsp;</a>
```python
@property
children(self): 
```
Returns the child objects for docs purposes
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_children" class="docs-object-method">&nbsp;</a>
```python
resolve_children(self, check_tree=True): 
```
Resolves the "children" of obj.
        First tries to use any info supplied by the docs tree
        or a passed object spec, then that failing looks for an
        `__all__` attribute
- `obj`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_object" class="docs-object-method">&nbsp;</a>
```python
resolve_object(o): 
```
Resolves to an arbitrary object by name
- `o`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.doc_spec" class="docs-object-method">&nbsp;</a>
```python
@property
doc_spec(self): 
```
Provides info that gets added to the `written` dict and which allows
        for a doc tree to be built out.
- `:returns`: `_`
    >No description...

<a id="Peeves.Peeves.Doc.Writers.DocWriter.parse_doc" class="docs-object-method">&nbsp;</a>
```python
parse_doc(self, doc): 
```

- `doc`: `str`
    >No description...
- `:returns`: `_`
    >No description...

### Examples


