## <a id="Peeves.Peeves.Doc.Writers.DocWriter">DocWriter</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L98)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L98?message=Update%20Docs)]
</div>

A general writer class that writes a file based off a template and filling in object template specs

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
 
### <a class="collapse-link" data-toggle="collapse" href="#methods">Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>

 </div>
 <div class="collapsible-section collapsible-section-body collapse" id="methods" markdown="1">

```python
template: str
template_root: str
template_name: str
default_template_base: str
examples_header: str
default_examples_root: str
default_tests_root: str
details_header: str
preformat_field_handlers: dict
protected_fields: set
default_fields: dict
outStream: type
blacklist_packages: set
param_template: str
```
<a id="Peeves.Peeves.Doc.Writers.DocWriter.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, obj, out_file, tree=None, name=None, parent=None, spec=None, template_directory=None, examples_directory=None, parent_tests=None, template=None, root=None, ignore_paths=None, examples=None, tests=None, formatter=None, include_line_numbers=True, include_link_bars=True, extra_fields=None, preformat_field_handlers=None, ignore_missing=False, strip_undocumented=False, **ext): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L124)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L124?message=Update%20Docs)]
</div>


- `formatter`: `Any`
    >object that can format the stuff that Markdown supports
- `tests`: `str | None`
    >path to tests to load
- `examples`: `str | None`
    >path to examples to load
- `ignore_paths`: `Iterable[str]`
    >paths to never write
- `root`: `str | None`
    >root directory to build off of
- `template`: `str | None`
    >template string to use when generating files
- `spec`: `dict | None`
    >extra parameters that are usually inherited from the parent writer
- `parent`: `Any`
    >parent object for docs purposes
- `name`: `Any`
    >name to be used in the docs
- `tree`: `Any`
    >tree of written docs for looking stuff up
- `out_file`: `str | None`
    >file to write to
- `obj`: `Any`
    >object to write

<a id="Peeves.Peeves.Doc.Writers.DocWriter.collapse_wrap_if_repo" class="docs-object-method">&nbsp;</a> 
```python
collapse_wrap_if_repo(self, header, content, name=None, open=True, include_opener=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L233)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L233?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.name" class="docs-object-method">&nbsp;</a> 
```python
@property
name(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Returns the name (not full identifier) of the object
being documented
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_name" class="docs-object-method">&nbsp;</a> 
```python
get_name(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L248)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L248?message=Update%20Docs)]
</div>

Returns the name the object will have in its documentation page
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.out" class="docs-object-method">&nbsp;</a> 
```python
@property
out(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.write_string" class="docs-object-method">&nbsp;</a> 
```python
write_string(self, txt): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L293)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L293?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.template_params" class="docs-object-method">&nbsp;</a> 
```python
template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L296)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L296?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_template_params" class="docs-object-method">&nbsp;</a> 
```python
get_template_params(self, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L303)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L303?message=Update%20Docs)]
</div>

Returns the parameters that should be inserted into the template
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.format" class="docs-object-method">&nbsp;</a> 
```python
format(self, template=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L324)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L324?message=Update%20Docs)]
</div>

Formats the documentation Markdown from the supplied template
- `:returns`: `_`
    >
- `template`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.check_should_write" class="docs-object-method">&nbsp;</a> 
```python
check_should_write(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L382)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L382?message=Update%20Docs)]
</div>

Determines whether the object really actually should be
documented (quite permissive)
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.write" class="docs-object-method">&nbsp;</a> 
```python
write(self, template=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L390)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L390?message=Update%20Docs)]
</div>

Writes the actual docs file
- `:returns`: `_`
    >
- `template`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_package_and_url" class="docs-object-method">&nbsp;</a> 
```python
get_package_and_url(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L403)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L403?message=Update%20Docs)]
</div>

Returns package name and corresponding URL for the object
being documented
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.package_path" class="docs-object-method">&nbsp;</a> 
```python
@property
package_path(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.load_template" class="docs-object-method">&nbsp;</a> 
```python
load_template(file): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L431)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L431?message=Update%20Docs)]
</div>

Loads the documentation template
for the object being documented
- `:returns`: `_`
    >
- `file`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_identifier" class="docs-object-method">&nbsp;</a> 
```python
get_identifier(o): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L444)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L444?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.identifier" class="docs-object-method">&nbsp;</a> 
```python
@property
identifier(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_lineno" class="docs-object-method">&nbsp;</a> 
```python
get_lineno(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L468)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L468?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resource_dir" class="docs-object-method">&nbsp;</a> 
```python
resource_dir(self, spec_key, base_root): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L475)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L475?message=Update%20Docs)]
</div>

Returns the directory for a given resource (e.g. examples or tests)
by trying a number of different possible locations
- `:returns`: `_`
    >
- `base_root`: `Any`
    >
- `spec_key`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.find_template" class="docs-object-method">&nbsp;</a> 
```python
find_template(self, template): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L537)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L537?message=Update%20Docs)]
</div>

Finds the appropriate template for the object by looking
in a variety of different locations
- `:returns`: `_`
    >
- `template`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.template_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
template_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.examples_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
examples_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Returns the directory in which to look for examples
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.examples_path" class="docs-object-method">&nbsp;</a> 
```python
@property
examples_path(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Provides the default examples path for the object
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.load_examples" class="docs-object-method">&nbsp;</a> 
```python
load_examples(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L588)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L588?message=Update%20Docs)]
</div>

Loads examples for the stored object if provided
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.tests_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
tests_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Returns the directory in which to look for tests
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.tests_path" class="docs-object-method">&nbsp;</a> 
```python
@property
tests_path(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Provides the default tests path for the object
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.load_tests" class="docs-object-method">&nbsp;</a> 
```python
load_tests(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L624)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L624?message=Update%20Docs)]
</div>

Loads tests for the stored object if provided
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.tests" class="docs-object-method">&nbsp;</a> 
```python
@property
tests(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.get_test_markdown" class="docs-object-method">&nbsp;</a> 
```python
get_test_markdown(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L658)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L658?message=Update%20Docs)]
</div>

<a id="Peeves.Peeves.Doc.Writers.DocWriter.parent" class="docs-object-method">&nbsp;</a> 
```python
@property
parent(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Returns the parent object for docs purposes
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_parent" class="docs-object-method">&nbsp;</a> 
```python
resolve_parent(self, check_tree=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L682)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L682?message=Update%20Docs)]
</div>

Resolves the "parent" of obj.
By default, just the module in which it is contained.
Allows for easy skipping of pieces of the object tree,
though, since a parent can be directly added to the set of
written object which is distinct from the module it would
usually resolve to.
Also can be subclassed to provide more fine grained behavior.
- `:returns`: `_`
    >
- `obj`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.children" class="docs-object-method">&nbsp;</a> 
```python
@property
children(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Returns the child objects for docs purposes
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_children" class="docs-object-method">&nbsp;</a> 
```python
resolve_children(self, check_tree=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L738)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L738?message=Update%20Docs)]
</div>

Resolves the "children" of obj.
First tries to use any info supplied by the docs tree
or a passed object spec, then that failing looks for an
`__all__` attribute
- `:returns`: `_`
    >
- `obj`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.resolve_object" class="docs-object-method">&nbsp;</a> 
```python
resolve_object(o): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L767)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L767?message=Update%20Docs)]
</div>

Resolves to an arbitrary object by name
- `:returns`: `_`
    >
- `o`: `Any`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.doc_spec" class="docs-object-method">&nbsp;</a> 
```python
@property
doc_spec(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L?message=Update%20Docs)]
</div>

Provides info that gets added to the `written` dict and which allows
for a doc tree to be built out.
- `:returns`: `_`
    >

<a id="Peeves.Peeves.Doc.Writers.DocWriter.parse_doc" class="docs-object-method">&nbsp;</a> 
```python
parse_doc(self, doc): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/Writers.py#L829)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L829?message=Update%20Docs)]
</div>


- `:returns`: `_`
    >
- `doc`: `str`
    >

 </div>
</div>


<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#Details-716208" markdown="1"> Details</a> <a class="float-right" data-toggle="collapse" href="#Details-716208"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="Details-716208" markdown="1">
 `DocWriter` objects are intended to do two things
 1. they manage the parsing logic to extract documentable parameters from objects
 2. they manage the process of loading the appropriate template and inserting the parameters
This double-duty nature is likely to change in a future version of the package, being delegated to two
subobjects that the writer then uses
 </div>
</div>





___

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Peeves/Doc/Writers/DocWriter.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Peeves/Doc/Writers/DocWriter.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Peeves/Doc/Writers/DocWriter.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Peeves/Doc/Writers/DocWriter.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/Writers.py#L98?message=Update%20Docs)