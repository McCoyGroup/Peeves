
import os

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

    defaults_root = os.path.dirname(__file__)
    default_templates_extension = 'templates'
    default_config_file="_config.yml"

    def __init__(self,
                 packages=None,
                 config=None,
                 target=None,
                 root=None,
                 config_file=None,
                 templates_directory=None,
                 examples_directory=None,
                 tests_directory=None,
                 readme=None
                 ):
        """
        :param packages: list of package configs to write
        :type packages: Iterable[str|dict]
        :param config: parameters for _config.yml file
        :type config: dict
        :param target: target directory to which files should be written
        :type target: str
        :param root: root directory
        :type root: str
        :param root: root directory
        :type root: str
        """
        self.packages = packages
        self.config = config
        self.target = target
        self.root = root
        self.template_dir = (
            os.path.join(self.defaults_root, self.default_templates_extension) if templates_directory is None else (
                templates_directory if os.path.isdir(templates_directory) else os.path.join(self.defaults_root, templates_directory)
            )
        )
        self.examples_dir=examples_directory
        self.tests_directory=tests_directory
        self.config_file=self.default_config_file if config_file is None else config_file

        if isinstance(readme, str):
            if os.path.isfile(readme):
                with open(readme) as r:
                    readme = r.read()
        self.readme=readme

    config_defaults = {
        "theme":"McCoyGroup/finx",
        "gh_username":"McCoyGroup-bot",
        "footer": ""
    }
    def load_config(self):
        """
        Loads the config file to be used and fills in template parameters

        :return:
        :rtype:
        """
        cfg = self.config_defaults.copy()
        if self.config is not None:
            cfg.update(**self.config)
        self.config = cfg

        test_cfg = os.path.join(self.template_dir, self.config_file)
        cfg_file = self.config_file if os.path.isfile(self.config_file) else (
            test_cfg if os.path.isfile(test_cfg) else os.path.join(self.template_dir, '_config.yml')
        )

        if os.path.isfile(cfg_file):
            with open(cfg_file) as config_dump:
                cfg_string = config_dump.read().format(**cfg)

            return cfg_string

    def create_layout(self):
        """
        Creates the documentation layout that will be expanded upon by
        a `DocWalker`

        :return:
        :rtype:
        """

        if self.config is not None:
            conf = self.load_config()
            if isinstance(conf, str):
                config_file = os.path.join(self.target, '_config.yml') # hard coded for now, can change later
                try:
                    os.makedirs(os.path.dirname(config_file))
                except OSError:
                    pass
                with open(config_file, 'w') as out:
                    out.write(conf)

        # do other layout stuff maybe in the future?

    def load_walker(self):
        """
        Loads the `DocWalker` used to write docs.
        A hook that can be overriden to sub in different walkers.

        :return:
        :rtype:
        """
        return DocWalker(
            self.packages,
            out=self.target,
            description=self.readme,
            extra_fields=self.config
        )

    def build(self):
        """
        Writes documentation layout to `self.target`

        :return:
        :rtype:
        """
        self.create_layout()
        walker = self.load_walker()
        return walker.write_docs()
