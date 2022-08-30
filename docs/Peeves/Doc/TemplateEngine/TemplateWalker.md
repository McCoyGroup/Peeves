## <a id="Peeves.Doc.TemplateEngine.TemplateWalker">TemplateWalker</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L?message=Update%20Docs)]
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
__init__(self, engine: Peeves.Peeves.Doc.TemplateEngine.TemplateEngine, out=None, **extra_fields): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker/__init__/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/__init__/__init__.py#L?message=Update%20Docs)]
</div>


<a id="str.default_handlers" class="docs-object-method">&nbsp;</a> 
```python
@property
default_handlers(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/default_handlers/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/default_handlers/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.get_handler" class="docs-object-method">&nbsp;</a> 
```python
get_handler(self, obj, *, out=None, engine=None, tree=None, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker/get_handler/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/get_handler/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.visit_root" class="docs-object-method">&nbsp;</a> 
```python
visit_root(self, o, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker/visit_root/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/visit_root/__init__.py#L?message=Update%20Docs)]
</div>


<a id="Peeves.Doc.TemplateEngine.TemplateWalker.write" class="docs-object-method">&nbsp;</a> 
```python
write(self, objects, index='index.md'): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Doc/TemplateEngine/TemplateWalker/write/__init__.py#L)/[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/write/__init__.py#L?message=Update%20Docs)]
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

[Edit Examples](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/Doc/TemplateEngine/TemplateWalker.md) or 
[Create New Examples](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/Doc/TemplateEngine/TemplateWalker.md) <br/>
[Edit Template](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/Doc/TemplateEngine/TemplateWalker.md) or 
[Create New Template](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/Doc/TemplateEngine/TemplateWalker.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Doc/TemplateEngine/TemplateWalker/__init__.py#L?message=Update%20Docs)