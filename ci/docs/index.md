# Peeves

Peeves is a documentation and unit testing package.
It started out as a very small layer on the `unittest` framework but now
supports the documentation for itself, as well as the [`Psience`](https://mccoygroup.github.io/Psience/) and [`McUtils`](https://mccoygroup.github.io/McUtils/) packages.
To use Peeves in your own projects, install via `pip`

```shell
pip install mccoygroup-peeves
```

and then to use Peeves to manage your unit tests, follow the pattern laid out in the [`ci/tests` directory](https://github.com/McCoyGroup/Peeves/tree/master/ci/tests).
You can also look at what was done for the [`McUtils` project](https://github.com/McCoyGroup/McUtils/tree/master/ci/tests).

To use the documentation generator, follow the pattern laid out in the [documentation build script](https://github.com/McCoyGroup/Peeves/tree/master/ci/build_docs.py).

#### API Reference

- [Peeves](Peeves.md)

## Examples

Running tests with `TestManager`.
We need to tell it where to start looking for tests.

```python
# set up paths
import os, sys
# provide the path to the directory with the tests
test_dir = os.path.dirname(os.path.abspath(__file__))
test_root = os.path.dirname(test_dir)
# provide the path to the test module to import
test_pkg = os.path.basename(test_dir)
sys.path.insert(0, os.path.dirname(test_root))

from Peeves.TestUtils import TestManager

TestManager.run(root=test_root, package=test_pkg)
```

---

Creating docs with `Peeves.Doc`

```python
import os
root = 'path/to/root/dir' # where are tests/templates/examples located
# with tempfile.TemporaryDirectory() as td:
td = 'target/directory'
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

---



### Help Us Out!

The easiest way to help us out is to _give feedback_.
Each page _should_ support examples, but unfortunately most do not, simply because writing that kind of thing by hand is time consuming.
If you see a page without examples and you want some, let us know!
To do that, just open and [issue on GitHub]((https://github.com/McCoyGroup/Peeves/issues/new?title=Documentation%20Improvement%20Needed)).
You can use the `Feedback` button at the bottom of each page to do so.

If you want to be a bit more proactive, feel free to provide examples and docstrings yourself! 
There are links at the bottom of each page to edit the examples, templates, and docstrings for that page.
Just create a new one if needed or edit the old one, commit your changes, and `Peeves` will rebuild the site
which what you've added.
It is a huge, huge help, so please take advantage of the opportunity if you're looking for ways to get involved.

