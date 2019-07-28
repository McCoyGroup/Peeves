"""Peeves is a minor extension to the unittest framework that makes my life better"""

from .TestUtils import *
from .Timer import *

from .TestUtils import __all__ as TU_all
from .Timer import __all__ as TI_all
__all__ = TU_all + TI_all + [ "Doc" ]