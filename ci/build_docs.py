import os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from Peeves import *
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
Doc.DocBuilder(**doc_config).build()