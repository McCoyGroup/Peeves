
from .DocWalker import DocWalker

__all__ = [
    "DocBuilder"
]

class DocBuilder:
    """
    A documentation builder class that uses a `DocWalker`
    to build documentation, but which also has support for more
    involved use cases, like setting up a `_config.yml` or other
    documentation template things.
    """
    def __init__(self,
                 packages=None,
                 config=None,
                 target=None,
                 root=None
                 ):
        """
        :param packages: list of package configs to write
        :type packages: Iterable[str|dict]
        :param config: parameter
        :type config: dict
        :param target: target directory to which files should be written
        :type target: str
        :param root: root directory
        :type root: str
        """
        self.packages = packages
        self.config = config

    def create_layout(self):
        """
        Creates the documentation layout that will be expanded upon by
        a `DocWalker`

        :return:
        :rtype:
        """


    def build(self):
        """
        Writes documentation layout to `self.target`

        :return:
        :rtype:
        """
        self.create_layout()
        walker = DocWalker(self.packages)

