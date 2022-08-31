## <a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker">TemplateWalker</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L906)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L906?message=Update%20Docs)]
</div>









<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse " id="methods" markdown="1">
 ```python
module_handler: ModuleTemplateHandler
class_handler: ClassTemplateHandler
function_handler: FunctionTemplateHandler
method_handler: MethodTemplateHandler
object_handler: ObjectTemplateHandler
index_handler: IndexTemplateHandler
```
<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, engine: Peeves.Peeves.Doc.TemplateEngine.TemplateEngine, out=None, description=None, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/__init__/__init__.py#L913)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/__init__/__init__.py#L913?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker.default_handlers" class="docs-object-method">&nbsp;</a> 
```python
@property
default_handlers(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/default_handlers/__init__.py#L919)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/default_handlers/__init__.py#L919?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker.get_handler" class="docs-object-method">&nbsp;</a> 
```python
get_handler(self, obj, *, out=None, engine=None, tree=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/get_handler/__init__.py#L928)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/get_handler/__init__.py#L928?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker.visit_root" class="docs-object-method">&nbsp;</a> 
```python
visit_root(self, o, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/visit_root/__init__.py#L937)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/visit_root/__init__.py#L937?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.Doc.TemplateEngine.TemplateWalker.write" class="docs-object-method">&nbsp;</a> 
```python
write(self, objects, index='index.md'): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/write/__init__.py#L940)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/write/__init__.py#L940?message=Update%20Docs)]
</div>
Walks through the objects supplied and applies the appropriate templates
  - `:returns`: `str`
    > i
n
d
e
x
 
o
f
 
w
r
i
t
t
e
n
 
f
i
l
e
s
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
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/TemplateWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/TemplateWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L906?message=Update%20Docs)   
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