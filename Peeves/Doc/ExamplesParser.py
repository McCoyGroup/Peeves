
import ast, collections, inspect

__all__ = [
    "ExamplesParser",
    "TestExamplesFormatter"
]

class ExamplesParser:
    """
    Provides a parser for unit tests to turn them into examples
    """

    def __init__(self, unit_tests):
        self.source = unit_tests
        self.ast = ast.parse(unit_tests)
        self._class_node = None
        self._setup = None
        self._functions = None

    def find_setup(self, tree_iter):
        setup = []
        for node in tree_iter:
            node_type = type(node).__name__
            if node_type not in ["ClassDef"]:
                setup.append(node)
            else:
                break
        else:
            node = None
        return node, setup

    def parse_tests(self, tree_iter):
        """
        Parses out the
        :param tree_iter:
        :type tree_iter:
        :return:
        :rtype:
        """
        class_setup = []
        functions = collections.OrderedDict()
        for node in tree_iter:
            node_type = type(node).__name__
            if node_type == 'FunctionDef':
                fname = node.name
                if fname.startswith('test_'):
                    functions[fname.split("_", 1)[1]] = node
                else:
                    class_setup.append(node)
            else:
                class_setup.append(node)
            # else:
            #     raise ValueError(
            #         "AST node of type {} with body {} not handled".format(
            #             node_type, ast.get_source_segment(self.source, node)
            #         )
            #     )
        return class_setup, functions

    def walk_tree(self):
        if hasattr(self.ast, 'body'):
            tree = self.ast.body
        else:
            tree = self.ast
        tree_iter = iter(tree)
        class_node, base_setup = self.find_setup(tree_iter)
        class_setup, functions = self.parse_tests(class_node.body)
        self._class_node = class_node
        self._setup = (base_setup, class_setup)
        self._functions = functions
        return self._setup, self._functions

    def format_node(self, node):
        base = ast.get_source_segment(self.source, node)
        indent = " "*node.col_offset
        return indent + base

    @classmethod
    def from_file(cls, tests_file):
        with open(tests_file) as f:
            return cls(f.read())

    @property
    def class_spec(self):
        if self._class_node is None:
            self.walk_tree()
        return (self._class_node, self._setup[1])
    @property
    def setup(self):
        if self._setup is None:
            self.walk_tree()
        return self._setup[0]
    @property
    def functions(self):
        if self._functions is None:
            self.walk_tree()
        return self._functions

class TestExamplesFormatter:
    def __init__(self, unit_tests, template=None, example_template=None):
        self.parser = ExamplesParser(unit_tests)
        self.template = inspect.cleandoc(self.default_template) if template is None else template
        self.example_template = inspect.cleandoc(self.default_example_template) if example_template is None else example_template
    @classmethod
    def from_file(cls, tests_file):
        with open(tests_file) as f:
            return cls(f.read())

    default_template = """
    ### Tests
    {links}
    
    #### Setup
    Before we can run our examples we should get a bit of setup out of the way.
    Since these examples were harvested from the unit tests not all pieces
    will be necessary for all situations.
    ```python
    {setup}
    ```
    
    All tests are wrapped in a test class
    ```python
    {class_setup}
    ```
    {tests}
    """
    def format(self):
        """
        Formats an examples file

        :return:
        :rtype:
        """
        imports = self.parser.setup
        setup = "\n".join(self.parser.format_node(node) for node in imports)

        cls = self.parser.class_spec
        class_setup = "\n".join(
            [
                "class {}({}):".format(
                    cls[0].name,
                    ",".join(x.id for x in cls[0].bases)
                ),
                *(self.parser.format_node(node) for node in cls[1])
            ]
        )

        links = self.format_jump_links(self.parser.functions)
        tests = self.format_examples()

        return self.template.format(
            links=links,
            setup=setup,
            class_setup=class_setup,
            tests=tests
        )

    def format_jump_links(self, functions):
        return "\n".join(
            "- [{k}](#{k})".format(k=k) for k in functions.keys()
        )

    default_example_template = """
        #### <a name="{name}">{name}</a>
        ```python
        {body}
        ```
        """
    def format_examples(self):
        return "\n".join(
            self.example_template.format(
                name=k,
                body=self.parser.format_node(v)
            )
            for k,v in self.parser.functions.items()
        )