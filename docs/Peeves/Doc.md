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










---


<div markdown="1" class="text-secondary fs-3">
<div class="container">
  <div class="row">
   <div class="col" markdown="1">
[Give Feedback](https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)   
</div>
   <div class="col" markdown="1">
   
</div>
   <div class="col" markdown="1">
   
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
**Examples**   
</div>
   <div class="col" markdown="1">
**Template**   
</div>
   <div class="col" markdown="1">
**Documentation**   
</div>
</div>
  <div class="row">
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/__init__.py#L1?message=Update%20Docs)   
</div>
</div>
</div>
</div>