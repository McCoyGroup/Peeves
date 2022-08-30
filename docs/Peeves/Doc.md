# <a id="Peeves.Doc">Peeves.Doc</a> 
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py#L?message=Update%20Docs)]
</div>
    
Simple Documentation framework that takes all of the python docstrings and unwraps them into proper docs while supporting
example and template files.

<div class="container alert alert-secondary bg-light">
  <div class="row">
   <div class="col" markdown="1">
[DocBuilder](Peeves/Doc/DocsBuilder/DocBuilder.md)   
</div>
   <div class="col" markdown="1">
[DocWalker](Peeves/Doc/DocWalker/DocWalker.md)   
</div>
   <div class="col" markdown="1">
[ModuleWriter](Peeves/Doc/DocWalker/ModuleWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ClassWriter](Peeves/Doc/DocWalker/ClassWriter.md)   
</div>
   <div class="col" markdown="1">
[FunctionWriter](Peeves/Doc/DocWalker/FunctionWriter.md)   
</div>
   <div class="col" markdown="1">
[MethodWriter](Peeves/Doc/DocWalker/MethodWriter.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ObjectWriter](Peeves/Doc/DocWalker/ObjectWriter.md)   
</div>
   <div class="col" markdown="1">
[IndexWriter](Peeves/Doc/DocWalker/IndexWriter.md)   
</div>
   <div class="col" markdown="1">
[ExamplesParser](Peeves/Doc/ExamplesParser/ExamplesParser.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateFormatter](Peeves/Doc/TemplateEngine/TemplateFormatter.md)   
</div>
   <div class="col" markdown="1">
[FormatDirective](Peeves/Doc/TemplateEngine/FormatDirective.md)   
</div>
   <div class="col" markdown="1">
[TemplateFormatDirective](Peeves/Doc/TemplateEngine/TemplateFormatDirective.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateOps](Peeves/Doc/TemplateEngine/TemplateOps.md)   
</div>
   <div class="col" markdown="1">
[TemplateEngine](Peeves/Doc/TemplateEngine/TemplateEngine.md)   
</div>
   <div class="col" markdown="1">
[ResourceLocator](Peeves/Doc/TemplateEngine/ResourceLocator.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[TemplateResourceExtractor](Peeves/Doc/TemplateEngine/TemplateResourceExtractor.md)   
</div>
   <div class="col" markdown="1">
[TemplateWalker](Peeves/Doc/TemplateEngine/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[TemplateHandler](Peeves/Doc/TemplateEngine/TemplateHandler.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[ModuleTemplateHandler](Peeves/Doc/TemplateEngine/ModuleTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[ClassTemplateHandler](Peeves/Doc/TemplateEngine/ClassTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[FunctionTemplateHandler](Peeves/Doc/TemplateEngine/FunctionTemplateHandler.md)   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[MethodTemplateHandler](Peeves/Doc/TemplateEngine/MethodTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[ObjectTemplateHandler](Peeves/Doc/TemplateEngine/ObjectTemplateHandler.md)   
</div>
   <div class="col" markdown="1">
[IndexTemplateHandler](Peeves/Doc/TemplateEngine/IndexTemplateHandler.md)   
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





## Examples
Test example...












<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#Tests-21cf3d" markdown="1"> Tests</a> <a class="float-right" data-toggle="collapse" href="#Tests-21cf3d"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="Tests-21cf3d" markdown="1">
 - [PeevesDoc](#PeevesDoc)
- [ParseExamples](#ParseExamples)
- [FormatSpec](#FormatSpec)

<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
### <a class="collapse-link" data-toggle="collapse" href="#Setup-778db0" markdown="1"> Setup</a> <a class="float-right" data-toggle="collapse" href="#Setup-778db0"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="Setup-778db0" markdown="1">
 
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
                'url_base': "Peeves",
                "gh_username": "McCoyGroup",
                "gh_repo": "Peeves",
                "gh_branch": "master",
                "footer": "Brought to you by the McCoy Group"
            },
            "packages": [
                {
                    "id": "Peeves",
                    'examples_directory': os.path.join(root, "ci", "examples"),
                    'tests_directory': os.path.join(root, "ci", "tests")
                }
            ],
            "root": root,
            "target": target,
            "readme": os.path.join(root, "README.md")
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

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py#L?message=Update%20Docs)