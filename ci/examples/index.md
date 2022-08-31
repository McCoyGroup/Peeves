
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

