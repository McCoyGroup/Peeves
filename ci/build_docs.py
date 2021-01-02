from Peeves.Doc import *
import os

root = os.path.dirname(os.path.dirname(__file__))
target = os.path.join(root, "docs")
doc_config = {
    "config": {
        "theme": "McCoyGroup/finx",
        "title": "Peeves",
        "path": "Peeves",
        "url": "https://mccoygrp.github.io/Peeves/",
        "gh_username": "b3m2a1"
    },
    "packages": [
        {
            "id": "Peeves",
            'tests_root': os.path.join(root, "ci", "tests")
        }
    ],
    "root": root,
    "target": target
}
DocBuilder(**doc_config).build()