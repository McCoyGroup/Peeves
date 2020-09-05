"""
Simple Documentation framework that takes all of the python docstrings and unwraps them into proper docs while supporting
example and template files
"""

from .DocWalker import *
from .Writers import *

from .DocWalker import __all__ as DW_a
from .Writers import __all__ as W_a
__all__ = DW_a + W_a