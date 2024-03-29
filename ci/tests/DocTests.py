import inspect, os, sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)
from Peeves.TestUtils import *
from unittest import TestCase
from Peeves.Doc import *
import os

class DocsTests(TestCase):
    """
    Sample documentation generator tests
    """

    @debugTest
    def test_PeevesDoc(self):
        """
        Builds sample documentation for the Peeves package

        :return:
        :rtype:
        """

        import os, tempfile


        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # with tempfile.TemporaryDirectory() as td:
        td = '/var/folders/9t/tqc70b7d61v753jkdbjkvd640000gp/T/tmpo3b4ztrq/'
        target = os.path.join(td, "docs")
        doc_config = {
            "config": {
                "title": "Peeves",
                "path": "Peeves",
                "url": "https://mccoygroup.github.io/Peeves/",
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

    @validationTest
    def test_ParseExamples(self):
        parser = ExamplesParser.from_file(os.path.abspath(__file__))
        self.assertTrue(hasattr(parser.functions, 'items'))
        tests = TestExamplesFormatter.from_file(os.path.abspath(__file__))
        print(tests.format())

    @validationTest
    def test_FormatSpec(self):

        fmt = inspect.cleandoc("""
        ### My Data
        
        {$:b=loop(add_temp, l1, l2, slots=['l1', 'l2'])}
        {$:len(b) ** 2}
        
        
        """)


        print("",
              TemplateFormatter().format(fmt, param=2, l1=[1, 2, 3], l2=[4, 5, 6], add_temp='{l1} + {l2}', p1=1, p2=0),
              sep="\n"
        )

