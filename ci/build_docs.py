from Peeves.Doc import *
import os

root = os.path.dirname(os.path.dirname(__file__))
target = os.path.join(root, "docs")
doc_config = {
    "config": {
        "title": "Peeves",
        "path": "Peeves",
        "url": "https://mccoygroup.github.io/Peeves/",
        "gh_username": "McCoyGroup",
        "footer": "Brought to you by the McCoy Group"
    },
    "packages": [
        {
            "id": "Peeves",
            'tests_root': os.path.join(root, "ci", "tests")
        }
    ],
    "root": root,
    "target": target,
    "readme": os.path.join(root, "README.md")
}
DocBuilder(**doc_config).build()