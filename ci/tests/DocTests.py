import inspect

from Peeves.TestUtils import *
from unittest import TestCase
from Peeves.Doc import *
import os

class DocsTests(TestCase):
    """
    Sample documentation generator tests
    """

    @validationTest
    def test_PeevesDoc(self):
        """
        Builds sample documentation for the Peeves package

        :return:
        :rtype:
        """

        import os

        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        target = os.path.expanduser("~/Desktop/docs")
        doc_config = {
            "config": {
                "theme": "McCoyGroup/finx",
                "title": "Peeves",
                "path": "",
                "url": "https://mccoygrp.github.io/Peeves/"
            },
            "packages": [
                {
                    "id": "Peeves",
                    'tests_root': os.path.join(root, "ci", "tests")
                }
            ],
            "root": root,
            "target": target,
            'readme': os.path.join(root, "README.md")
        }
        DocBuilder(**doc_config).build()

    @validationTest
    def test_ParseExamples(self):
        parser = ExamplesParser.from_file(os.path.abspath(__file__))
        self.assertTrue(hasattr(parser.functions, 'items'))
        tests = TestExamplesFormatter.from_file(os.path.abspath(__file__))
        print(tests.format())

    @debugTest
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

