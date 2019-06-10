"""This is the test running script set up to run all tests
Peeves should be embedded in a project as a submodule at the top level
This will mean there is a "..Tests" package to load the tests from

"""

import os, sys, argparse
from .TestUtils import TestManager, TestRunner, DebugTests, ValidationTests, TimingTests, LoadTests

#####################################################################################################################
#
#                                           PARSE ARGS
#

# Create ArgParser to take command line data and make it visible
parser = argparse.ArgumentParser(description='Process test configurations')
parser.add_argument('-q', dest='quiet', metavar='-q',
                       type=bool, nargs='?', default=TestManager.quiet_mode,
                       help='whether to run the tests in quiet mode')
parser.add_argument('-d', dest='debug', metavar='-d',
                       type=bool, nargs='?', default=TestManager.debug_tests,
                       help='whether to run the debug tests')
parser.add_argument('-v', dest='validate', metavar='-v',
                       type=bool, nargs='?', default=TestManager.validation_tests,
                       help='whether to run the validation tests')
parser.add_argument('-t', dest='timing', metavar='-t',
                       type=bool, nargs='?', default=TestManager.timing_tests,
                       help='whether to run the timing tests')
parser.add_argument('-l', dest='log', metavar='-l',
                       type=bool, nargs='?', default=TestManager.log_results,
                       help='whether to log results')
parser.add_argument('-L', dest='logfile', metavar='-L',
                       type=str, nargs='?', default=TestManager.log_file,
                       help='whether to log results')
parser.add_argument('-f', dest='testfile', metavar='-f',
                       type=str, nargs='?', default=TestManager.test_files,
                       help='which tests to run')
args = parser.parse_args()
quiet = args.quiet
debug = args.debug
validate = args.validate
timing = args.timing
log_results = args.log
log_file = args.logfile

#####################################################################################################################
#
#                                          LOAD TESTS
#

if args.testfile.lower() == "all":
    TestManager.test_files = "All"
else:
    TestManager.test_files = args.testfile.split(",")

LoadTests(TestManager.base_dir)


#####################################################################################################################
#
#                                       CONFIGURE LOGGING
#

v_level = 1 if quiet else 2
if os.path.abspath(log_file) != log_file:
    log_file = os.path.join(TestManager.test_dir, log_file)
log_stream = open(log_file, "w") if log_results else sys.stderr
stderr1 = sys.stderr

#####################################################################################################################
#
#                                          RUN TESTS
#

def run_tests(tag, test_set, runner, log_stream):
    print(
            "\n"+"-"*70+"\n"+"-"*70+"\n"+
                "Running {} Tests:\n".format(tag),
        file=log_stream
    )
    return runner.run(test_set)
try:
    sys.stderr = log_stream
    runner = TestRunner(stream = log_stream, verbosity=v_level)

    debug_results= None
    if debug:
        debug_results  = run_tests("Debug", DebugTests, runner, log_stream)

    validate_results= None
    if validate:
        validate_results  = run_tests("Validation", ValidationTests, runner, log_stream)

    timing_results= None
    if timing:
        timing_results  = run_tests("Timing", TimingTests, runner, log_stream)

    debug_status = (debug_results is None) or debug_results.wasSuccessful()
    timing_status = (timing_results is None) or timing_results.wasSuccessful()
    validate_status = (validate_results is None) or validate_results.wasSuccessful()
    test_status = not (debug_status & timing_status & validate_status)

finally:
    sys.stderr = stderr1



