"""
All of the utilities that are used in writing tests for Peeves
"""

from .Timer import Timer
import unittest, numpy as np, os, sys

__all__ = [
    "TestRunner",
    "DebugTests",
    "ValidationTests",
    "TimingTests",
    "LoadTests",
    "TestManager",
    "DataGenerator",
    "load_tests",
    "validationTest",
    "debugTest",
    "timeitTest",
    "timingTest"
]

class TestManagerClass:
    """Just manages where things load from
    """
    log_file = "test_results.txt"
    log_results = False
    quiet_mode = False
    debug_tests = True
    validation_tests = False
    timing_tests = False
    test_files = "All"
    def __init__(self,
                 test_root = None, test_dir = None, test_data = None,
                 base_dir = None, test_pkg = "Tests", test_data_ext = "TestData"
                 ):
        self._base_dir = base_dir
        self._test_root = test_root
        self._base_dir_use_default = base_dir is None
        self._test_dir = test_dir
        self._test_dir_use_default = test_dir is None
        self._test_data = test_data
        self._test_data_use_default = test_data is None
        self._test_pkg = test_pkg
        self._test_pkg_validated = False
        self.data_ext = test_data_ext
    @property
    def test_root(self):
        if self._test_root is None:
            try:
                test_root = [ a for a in sys.argv if os.path.isdir(a) ][0] # you can pass the directory to run the tests as the first sys.argv arg
            except IndexError:
                test_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # or we'll assume it's two dirs up from here
            sys.path.insert(0, test_root) # not sure exactly what this does... might want to be more targeted with it
            self._test_root = test_root
        return self._test_root
    @test_root.setter
    def test_root(self, root):
        self._test_root = root
        if self._base_dir_use_default:
            self._base_dir = None
        if self._test_dir_use_default:
            self._test_dir = None
        if self._test_data_use_default:
            self._test_data = None
    @property
    def base_dir(self):
        if self._base_dir is None:
            self._base_dir = os.path.dirname(self.test_root)
        return self._base_dir
    @base_dir.setter
    def base_dir(self, d):
        self._base_dir = d
        if d is not None:
            self._base_dir_use_default = False
    @property
    def test_pkg(self):
        if not self._test_pkg_validated:
            root = self.test_root
            # TODO: find some way to check it to figure out how many . we need to go up...
            # for now we'll just leave it, though
            if "." not in self._test_pkg:
                self._test_pkg = "."*(len(__package__.split(".")) - 1) + self._test_pkg
                # a basic guess as to what'll get us to the right spot...
            self._test_pkg_validated = True
        return self._test_pkg
    @test_pkg.setter
    def test_pkg(self, pkg):
        self._test_pkg = pkg
        self._test_pkg_validated = False
    @property
    def test_dir(self):
        # the Tests package _must_ be in the parent repository
        if self._test_dir is None:
            self._test_dir = os.path.join(self.test_root, self.test_pkg.split(".")[-1])
            if not os.path.isdir(self._test_dir) and self.test_pkg[0] == ".":
                raise Exception(
                    "Peeves expects a '{}' package at {} to hold all the tests because I wrote it bad",
                    self.test_pkg,
                    self.test_root
                    )
        return self._test_dir
    @test_dir.setter
    def test_dir(self, d):
        self._test_dir = d
        if d is not None:
            self._test_dir_use_default = False
    @property
    def test_data_dir(self):
        if self._test_data is None:
            self._test_data = os.path.join(self.test_dir, self.data_ext)
        return self._test_data
    @test_data_dir.setter
    def test_data_dir(self, d):
        self._test_data = d
        if d is not None:
            self._test_data_use_default = False
    def test_data(self, filename):
        return os.path.join(self.test_data_dir, filename)
    def run(self, exit = True):
        from .run_tests import test_status
        if exit:
            sys.exit(test_status) #should kill everything...?
        return test_status
TestManager = TestManagerClass()

TestCase = unittest.TestCase #just in case I want to change this up later
class DataGenerator:
    """Provides methods to generate relevant data for testing methods
    """

    @staticmethod
    def coords(n=50):
        return np.random.rand(n, 3)
    @staticmethod
    def multicoords(n=10, m=50):
        return np.random.rand(n, m, 3)
    @staticmethod
    def mats(n=1):
        return np.random.rand(n, 3, 3)
    @staticmethod
    def vecs(n=1):
        return np.random.rand(n, 3)

    @staticmethod
    def angles(n=50, r=(0, 360), use_rad=False):
        angles = np.random.uniform(*r, size=(n,))
        if use_rad:
            angles = np.rad2deg(angles)
        return angles
    @staticmethod
    def dists(n=50, minmax=(.5, 1.5)):
        return np.random.uniform(*minmax, size=(n,))
    @staticmethod
    def zmat(ncoords=15, use_rad=False):
        refs1 = np.sort(np.random.randint(0, ncoords, ncoords))
        refs2 = np.sort(np.random.randint(0, ncoords, ncoords))
        refs3 = np.sort(np.random.randint(0, ncoords, ncoords))
        ass = np.arange(0, ncoords)
        refs1 = np.amin(np.array((refs1, ass)), axis=0)
        refs2 = np.amin(np.array((refs2, ass)), axis=0)
        for i,rs in enumerate(zip(refs1, refs2)):
            r1, r2 = rs
            if i > 0 and r1 == r2:
                while r1 == r2:
                    r2 = (r2 + 1) % (i + 1)
                    # print(r1, r2, i)
                refs2[i] = r2
        refs3 = np.amin(np.array((refs3, ass)), axis=0)
        for i,rs in enumerate(zip(refs1, refs2, refs3)):
            r1, r2, r3 = rs
            if i > 1 and (r1 == r3 or r2 == r3):
                while (r1 == r3 or r2 == r3):
                    r3 = (r3 + 1) % (i + 1)
                refs3[i] = r3

        # raise Exception(np.array((refs1, refs1-refs2, refs1-refs3, refs2-refs3)))
        dists = DataGenerator.dists(ncoords)
        angles = DataGenerator.angles(ncoords, (0, 180), use_rad=use_rad)
        dihedrals = DataGenerator.angles(ncoords, (0, 360), use_rad=use_rad)

        return np.array([refs1+1, dists, refs2+1, angles, refs3+1, dihedrals ]).T
    @staticmethod
    def zmats(m=10, ncoords=15, use_rad=False):
        return np.array([DataGenerator.zmat(ncoords, use_rad) for i in range(m)])

class DebugTestClass(unittest.TestSuite):
    """The set of fast tests in the test suite"""
    pass
DebugTests = DebugTestClass()
class ValidationTestClass(unittest.TestSuite):
    """The set of slow tests in the test suite"""
    pass
ValidationTests = ValidationTestClass()
class TimingTestClass(unittest.TestSuite):
    """The set of fast tests in the test suite"""
    pass
TimingTests = TimingTestClass()

def timingTest(fn):
    timer = Timer()(fn)
    def Timing(*args, **kwargs):
        return timer(*args, **kwargs)
    return Timing
def timeitTest(**kwargs):
    timer = Timer(**kwargs)
    def wrap(fn):
        inner_fn = timer(fn)
        def Timing(*args, **kwargs):
            return inner_fn(*args, **kwargs)
        return Timing
    return wrap

def debugTest(fn):
    def Debug(*args, **kwargs):
        return fn(*args, **kwargs)
    return Debug

def validationTest(fn):
    def Validation(*args, **kwargs):
        return fn(*args, **kwargs)
    return Validation

def TestRunner(**kw):
    if not "resultclass" in kw:
        kw["resultclass"] = unittest.TextTestResult
    if not "verbosity" in kw:
        kw["verbosity"] = 2
    return unittest.TextTestRunner(**kw)

_test_loader_map = {
    "Debug" : DebugTests,
    "Validation": ValidationTests,
    "Timing" : TimingTests
}

class ManagedTestLoader:
    manager = TestManager
    @classmethod
    def load_tests(cls, loader, tests, pattern):
        from itertools import chain

        pkgs = cls.manager.test_files
        test_packages = None if pkgs == "All" else set(pkgs)
        if test_packages is None:
            tests = list(chain(*((t for t in suite) for suite in tests)))
        else:
            def _get_suite_name(suite):
                for test in suite:
                    return type(test).__module__.split(".")[-1]
            tests_named = {_get_suite_name(suite):suite for suite in tests}
            tests = []
            for k in tests_named:
                if k in test_packages:
                    tests.extend(tests_named[k])
        for test in tests:
            method = getattr(test, test._testMethodName)
            ttt = method.__name__
            if ttt not in _test_loader_map:
                ttt = "Debug"
            suite = _test_loader_map[ttt]
            suite.addTest(test)
        #
        # return _test_loader_map.values()

load_tests = ManagedTestLoader.load_tests

def LoadTests(start_dir, manager = TestManager):
    ManagedTestLoader.manager = TestManager
    unittest.defaultTestLoader.discover(start_dir)
