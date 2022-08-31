## <a id="Peeves.Doc.TemplateEngine.TemplateWalker">TemplateWalker</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine.py#L859)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine.py#L859?message=Update%20Docs)]
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
<a id="Peeves.Doc.TemplateEngine.TemplateWalker.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, engine: Peeves.Peeves.Doc.TemplateEngine.TemplateEngine, out=None, description=None, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L866)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L866?message=Update%20Docs)]
</div>


<a id="str.default_handlers" class="docs-object-method">&nbsp;</a> 
```python
@property
default_handlers(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/default_handlers.py#L872)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/default_handlers.py#L872?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.get_handler" class="docs-object-method">&nbsp;</a> 
```python
get_handler(self, obj, *, out=None, engine=None, tree=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L881)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L881?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.visit_root" class="docs-object-method">&nbsp;</a> 
```python
visit_root(self, o, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L890)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L890?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.write" class="docs-object-method">&nbsp;</a> 
```python
write(self, objects, index='index.md'): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L893)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker.py#L893?message=Update%20Docs)]
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
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/TemplateEngine/TemplateWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/TemplateEngine/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/TemplateEngine/TemplateWalker.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/TemplateEngine/TemplateWalker.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine.py#L859?message=Update%20Docs)   
</div>
</div>
</div>
</div>