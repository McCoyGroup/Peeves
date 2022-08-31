# <a id="Peeves.Doc">Peeves.Doc</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/__init__.py#L1)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py#L1?message=Update%20Docs)]
</div>
    
A simple documentation framework, similar to Sphinx.
It builds off of a template engine (provided by the `TemplateEngine` package) and an object-tree traversal
class (`TemplateWalker`) to fill out templates for the different types of python objects.
These templates are exported as Markdown so that they can be turned into a final website by a more sophisticated
Markdown -> HTML static site generator, like Jekyll.
Templates are extremely customizable (down to the object-level) with a flexible and powerful template mini-language
that builds off of python's built-in AST module and syntax.
Examples are also possible to provide for individual objects/modules and can also be harvested automatically from
unit tests if provided.

### Members
<div class="container alert alert-secondary bg-light">
  <div class="row">
   <div class="col" markdown="1">
[DocBuilder](Doc/DocsBuilder/DocBuilder.md)   
</div>
   <div class="col" markdown="1">
[DocWalker](Doc/DocWalker/DocWalker.md)   
</div>
   <div class="col" markdown="1">
[ModuleWriter](Doc/DocWalker/ModuleWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ClassWriter](Doc/DocWalker/ClassWriter.md)   
</div>
   <div class="col" markdown="1">
[FunctionWriter](Doc/DocWalker/FunctionWriter.md)   
</div>
   <div class="col" markdown="1">
[MethodWriter](Doc/DocWalker/MethodWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ObjectWriter](Doc/DocWalker/ObjectWriter.md)   
</div>
   <div class="col" markdown="1">
[IndexWriter](Doc/DocWalker/IndexWriter.md)   
</div>
   <div class="col" markdown="1">
[ExamplesParser](Doc/ExamplesParser/ExamplesParser.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateFormatter](Doc/TemplateEngine/TemplateFormatter.md)   
</div>
   <div class="col" markdown="1">
[FormatDirective](Doc/TemplateEngine/FormatDirective.md)   
</div>
   <div class="col" markdown="1">
[TemplateFormatDirective](Doc/TemplateEngine/TemplateFormatDirective.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateOps](Doc/TemplateEngine/TemplateOps.md)   
</div>
   <div class="col" markdown="1">
[TemplateEngine](Doc/TemplateEngine/TemplateEngine.md)   
</div>
   <div class="col" markdown="1">
[ResourceLocator](Doc/TemplateEngine/ResourceLocator.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateResourceExtractor](Doc/TemplateEngine/TemplateResourceExtractor.md)   
</div>
   <div class="col" markdown="1">
[TemplateWalker](Doc/TemplateEngine/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[TemplateHandler](Doc/TemplateEngine/TemplateHandler.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ModuleTemplateHandler](Doc/TemplateEngine/ModuleTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[ClassTemplateHandler](Doc/TemplateEngine/ClassTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[FunctionTemplateHandler](Doc/TemplateEngine/FunctionTemplateHandler.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[MethodTemplateHandler](Doc/TemplateEngine/MethodTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[ObjectTemplateHandler](Doc/TemplateEngine/ObjectTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[IndexTemplateHandler](Doc/TemplateEngine/IndexTemplateHandler.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
</div>

The templates provided are for modules, classes, methods, functions, and generic objects.
The mini-language used extends standard python string formatting syntax but allows for the
evaluation of a whitelisted set of commands within templates.
A full HTML/Bootstrap generator is included to allow for total customization of the generated
Markdown.
See `TemplateOps`, `TemplateFormatDirective`, `MarkdownOps`, and `MarkdownFormatDirective` for more info.



## Examples














<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#Tests-36fc24" markdown="1"> Tests</a> <a class="float-right" data-toggle="collapse" href="#Tests-36fc24"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="Tests-36fc24" markdown="1">
 - [PeevesDoc](#PeevesDoc)
- [ParseExamples](#ParseExamples)
- [FormatSpec](#FormatSpec)

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#Setup-f54f52" markdown="1"> Setup</a> <a class="float-right" data-toggle="collapse" href="#Setup-f54f52"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="Setup-f54f52" markdown="1">
 
Before we can run our examples we should get a bit of setup out of the way.
Since these examples were harvested from the unit tests not all pieces
will be necessary for all situations.

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

        import os, tempfile


        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # with tempfile.TemporaryDirectory() as td:
        td = '/var/folders/9t/tqc70b7d61v753jkdbjkvd640000gp/T/tmpo3b4ztrq/'
        target = os.path.join(td, "docs")
        doc_config = {
            "config": {
                "title": "Peeves",
                "path": "Peeves",
                "url": "https://mccoygroup.github.io/Peeves/",
                "gh_username": "McCoyGroup",
                "gh_repo": "Peeves",
                "gh_branch": "master",
                "footer": "Brought to you by the McCoy Group"
            },
            "packages": [
                {
                    "id": "Peeves"
                }
            ],
            "root": root,
            "target": target,
            "readme": os.path.join(root, "blurb.md"),
            'examples_directory': os.path.join(root, "ci", "examples"),
            'tests_directory': os.path.join(root, "ci", "tests"),
            'templates_directory': os.path.join(root, "ci", "templates")
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

#### <a name="FormatSpec">FormatSpec</a>
```python
    def test_FormatSpec(self):

        fmt = inspect.cleandoc("""
        ### My Data
        
        {$:b=loop(add_temp, l1, l2, slots=['l1', 'l2'])}
        {$:len(b) ** 2}
        
        
        """)


        print("",
              TemplateFormatter().format(fmt, param=2, l1=[1, 2, 3], l2=[4, 5, 6], add_temp='{l1} + {l2}', p1=1, p2=0),
              sep="\n"
        )
```

 </div>
</div>






---


<div markdown="1" class="text-secondary">
<div class="container">
  <div class="row">
   <div class="col" markdown="1">
**Feedback**   
</div>
   <div class="col" markdown="1">
**Examples**   
</div>
   <div class="col" markdown="1">
**Templates**   
</div>
   <div class="col" markdown="1">
**Documentation**   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[Bug](https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)/[Request](https://github.com/McCoyGroup/Peeves/issues/new?title=Example%20Request)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py#L1?message=Update%20Docs)   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
</div>
</div>
</div>
</div>