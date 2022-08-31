## <a id="Peeves.Peeves.TestUtils.TestManager">TestManager</a> 

<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils.py#L24)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils.py#L24?message=Update%20Docs)]
</div>

Manages the run of the tests







<div class="collapsible-section">
 <div class="collapsible-section collapsible-section-header" markdown="1">
## <a class="collapse-link" data-toggle="collapse" href="#methods" markdown="1"> Methods and Properties</a> <a class="float-right" data-toggle="collapse" href="#methods"><i class="fa fa-chevron-down"></i></a>
 </div>
 <div class="collapsible-section collapsible-section-body collapse show" id="methods" markdown="1">
 ```python
log_file: str
log_results: bool
quiet_mode: bool
debug_tests: bool
validation_tests: bool
timing_tests: bool
data_gen_tests: bool
test_files: str
test_name: NoneType
```
<a id="Peeves.Peeves.TestUtils.TestManager.__init__" class="docs-object-method">&nbsp;</a> 
```python
__init__(self, test_root=None, test_dir=None, test_data=None, base_dir=None, start_dir=None, test_pkg=None, test_data_ext='TestData', log_file=None, log_results=None, quiet_mode=None, debug_tests=None, validation_tests=None, timing_tests=None, data_gen_tests=None, test_files=None, test_name=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L38)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L38?message=Update%20Docs)]
</div>

  - `test_root`: `Any`
    > the root package
  - `test_dir`: `Any`
    > the directory to load tests from (usually test_root/test_pkg)
  - `test_data`: `Any`
    > the directory to load test data from (usually test_dir/test_data_ext)
  - `base_dir`: `Any`
    > the overall base directory to do imports from
  - `start_dir`: `Any`
    > the directory to start test discovery from
  - `test_pkg`: `Any`
    > the name of the python package that holds all the tests
  - `test_data_ext`: `Any`
    > the extension from test_dir to look for data in (usually TestData)


<a id="Peeves.Peeves.TestUtils.TestManager.test_root" class="docs-object-method">&nbsp;</a> 
```python
@property
test_root(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L98)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L98?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.base_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
base_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L117)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L117?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.start_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
start_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L127)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L127?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.test_pkg" class="docs-object-method">&nbsp;</a> 
```python
@property
test_pkg(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L137)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L137?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.test_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
test_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L154)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L154?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.test_data_dir" class="docs-object-method">&nbsp;</a> 
```python
@property
test_data_dir(self): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L172)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L172?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.test_data" class="docs-object-method">&nbsp;</a> 
```python
test_data(self, filename): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L182)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L182?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.collect_run_args" class="docs-object-method">&nbsp;</a> 
```python
collect_run_args(): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L185)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L185?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.get_log_file" class="docs-object-method">&nbsp;</a> 
```python
get_log_file(self, log_results=None, log_file=None, syserr_redirect=True): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L235)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L235?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.run_tests" class="docs-object-method">&nbsp;</a> 
```python
run_tests(self, tag, test_set, runner, log_stream): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L267)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L267?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.get_test_types" class="docs-object-method">&nbsp;</a> 
```python
get_test_types(self, debug=None, validate=None, timing=None, data_gen=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L275)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L275?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.load_tests" class="docs-object-method">&nbsp;</a> 
```python
load_tests(self, start_dir=None, base_dir=None): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L306)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L306?message=Update%20Docs)]
</div>


<a id="Peeves.Peeves.TestUtils.TestManager.run" class="docs-object-method">&nbsp;</a> 
```python
run(exit=True, exit_code=None, syserr_redirect=True, cmd_line=False, **kwargs): 
```
<div class="docs-source-link" markdown="1">
[[source](https://github.com/McCoyGroup/Peeves/blob/master/Peeves/Peeves/TestUtils/TestManager.py#L322)/
[edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils/TestManager.py#L322?message=Update%20Docs)]
</div>
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
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/examples/Peeves/TestUtils/TestManager.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/examples/Peeves/TestUtils/TestManager.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/gh-pages/ci/docs/Peeves/TestUtils/TestManager.md)/[New](https://github.com/McCoyGroup/Peeves/new/gh-pages/?filename=ci/docs/templates/Peeves/TestUtils/TestManager.md)   
</div>
   <div class="col" markdown="1">
[Edit](https://github.com/McCoyGroup/Peeves/edit/master/Peeves/Peeves/TestUtils.py#L24?message=Update%20Docs)   
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