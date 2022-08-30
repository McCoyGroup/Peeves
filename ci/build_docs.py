from Peeves.Doc import *
import os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target = os.path.join(root, "ci", "docs")
sys.path.insert(0, root)
doc_config = {
    "config": {
        "title": "Peeves",
        "path": "Peeves",
        "url": "https://mccoygroup.github.io/Peeves/",
        'url_base':"Peeves",
        "gh_username": "McCoyGroup",
        "gh_repo": "Peeves",
        "gh_branch": "master",
        "footer": "Brought to you by the McCoy Group"
    },
    "packages": [
        {
            "id": "Peeves",
            'tests_directory': os.path.join(root, "ci", "tests"),
            'examples_directory': os.path.join(root, "ci", "examples")
        }
    ],
    "root": root,
    "target": target,
    "readme": os.path.join(root, "README.md")
}
DocBuilder(**doc_config).build()