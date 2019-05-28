"""This is the test running script set up to run *all* tests


"""

import os, sys

try:
    base_dir = sys.argv[1] # you can pass the directory to run the tests as the first sys.argv arg
except:
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__))) # or we'll it's two dirs up from here
sys.path.insert(0, base_dir)

# the Tests package _must_ be in the parent repository
tests_dir = os.path.join(base_dir, "Tests")
if not os.path.isdir(tests_dir):
    raise Exception("Peeves expects a Tests package to hold all tests because I wrote it bad")

test_data_dir = os.path.join(os.path.dirname(__file__), "TestData")
def test_data(filename):
    return os.path.join(test_data_dir, filename)

# we'll expose all our tests utils and stuff here...
from Tests import TestRunner, DebugTests, ValidationTests, TimingTests, LoadTests

LoadTests(base_dir)

quiet = False
quiet = quiet or ("-q" in sys.argv)

debug = True
debug = debug or ("-D" in sys.argv)

timing = False
timing = timing or ("-T" in sys.argv)

validate = False
validate = validate or ("-V" in sys.argv)

v_level = 1 if quiet else 2
log_file_name = "test_results.txt" # could change if it's worth it
log_file = os.path.join(tests_dir, log_file_name)
log_stream = open(log_file, "w") if ("-l" in sys.argv) else sys.stderr
stderr1 = sys.stderr
sys.stderr = log_stream
runner = TestRunner(stream = log_stream, verbosity=v_level)

debug_results= None
if debug:
    print("\n"+"-"*70, file=log_stream)
    print("-"*70, file=log_stream)
    print("Running Debug Tests:"+"\n", file=log_stream)
    debug_results  = runner.run(DebugTests)

validate_results= None
if validate:
    print("\n"+"-"*70, file=log_stream)
    print("-"*70, file=log_stream)
    print("Running Validation Tests:"+"\n", file=log_stream)
    validate_results  = runner.run(ValidationTests)

timing_results= None
if timing:
    print("\n"+"-"*70, file=log_stream)
    print("-"*70, file=log_stream)
    print("Running Timing Tests:"+"\n", file=log_stream)
    timing_results  = runner.run(TimingTests)

debug_status = (debug_results is None) or debug_results.wasSuccessful()
timing_status = (timing_results is None) or timing_results.wasSuccessful()
validate_status = (validate_results is None) or validate_results.wasSuccessful()
overall_status = not (debug_status & timing_status & validate_status)

sys.stderr = stderr1

sys.exit(overall_status)



