
import sys, os, numpy as np, itertools as ip
import cProfile, pstats, io

__all__ = [
    "BlockProfiler"
]


class BlockProfiler:
    """
    Simple class to profile a block of code
    """

    def __init__(self, name="Profile Block",
                 strip_dirs=None,
                 print_res=True,
                 sort_by='cumulative',
                 num_lines=50,
                 filter=None
                 ):
        """
        :param name: name of profiled block
        :type name: str
        :param strip_dirs: directory paths to strip from report
        :type strip_dirs: None | Iterable[str]
        """

        self.name = name
        self.strip_dirs = strip_dirs
        self.print_res = print_res
        self.sort_by = sort_by
        self.num_lines = num_lines
        self.filter = filter

    def __enter__(self):
        self.pr = cProfile.Profile()
        self.pr.enable()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pr.disable()
        s = io.StringIO()
        sortby = self.sort_by
        ps = pstats.Stats(self.pr, stream=s).sort_stats(sortby)
        filt = [self.num_lines]
        if self.filter is not None:
            if isinstance(self.filter, (int, float, str)):
                filter = [self.filter]
            else:
                filter = list(self.filter)
            filt = filter + filt
        ps.print_stats(*filt)
        self.stat_block = s.getvalue()
        s.close()

        if self.print_res:
            self.print_stats()

    def format_stats(self):
        stat_block = self.stat_block
        strip_dirs = self.strip_dirs
        if strip_dirs is not None:
            for d in self.strip_dirs:
                stat_block = stat_block.replace(d, "")
        return stat_block

    def print_stats(self):
        print("In block {}:\n\n{}".format(self.name, self.format_stats()))