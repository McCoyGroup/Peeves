## <a id="Peeves.Peeves.Profiler.BlockProfiler">BlockProfiler</a>
Simple class to profile a block of code

### Properties and Methods
<a id="Peeves.Peeves.Profiler.BlockProfiler.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, name='Profile Block', strip_dirs=None, print_res=True, sort_by='cumulative', num_lines=50, filter=None): 
```

- `name`: `str`
    >name of profiled block
- `strip_dirs`: `None | Iterable[str]`
    >directory paths to strip from report

<a id="Peeves.Peeves.Profiler.BlockProfiler.__enter__" class="docs-object-method">&nbsp;</a>
```python
__enter__(self): 
```

<a id="Peeves.Peeves.Profiler.BlockProfiler.__exit__" class="docs-object-method">&nbsp;</a>
```python
__exit__(self, exc_type, exc_val, exc_tb): 
```

<a id="Peeves.Peeves.Profiler.BlockProfiler.format_stats" class="docs-object-method">&nbsp;</a>
```python
format_stats(self): 
```

<a id="Peeves.Peeves.Profiler.BlockProfiler.print_stats" class="docs-object-method">&nbsp;</a>
```python
print_stats(self): 
```

### Examples


### Unit Tests
