

{$:test_links={loop_template$:
    """"- [{k}](#{k})""",
    k=names,
    joiner='\\n'
}}

{$:tests_setup={collapse$:'Setup', '''
Before we can run our examples we should get a bit of setup out of the way.
Since these examples were harvested from the unit tests not all pieces
will be necessary for all situations.

All tests are wrapped in a test class
```python
{class_setup}
```
'''
}}

{$:test_examples={loop_template$:"""
#### <a name="{name}">{name}</a>
```python
{body}
```
""",
    name=,
    body=,
    joiner='\\n'
}}

{collapse$:'## Tests',
    {join$:
        test_links,
        test_setup,
        test_examples
    }
}