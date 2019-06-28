"""Provides a little timer for testing

"""
import timeit, functools

class timed:
    def __init__(self, **kw):
        self.kw = kw

    def get_time_list(self, time_elapsed):
        run_time = [0, 0, time_elapsed]
        if run_time[2] > 60:
            run_time[1] = int(run_time[2] / 60)
            run_time[2] = run_time[2] % 60
            if run_time[1] > 60:
                run_time[0] = int(run_time[1] / 60)
                run_time[1] = run_time[1] % 60
        return run_time

    def __call__(self, fn):
        @functools.wraps(fn)
        def timed_fn(*args, **kwargs):
            import sys
            func = fn
            val = None
            time_elapsed = timeit.timeit("val = func(*args, **kwargs)", globals = locals(), **self.kw)
            run_time = self.get_time_list(time_elapsed)
            run_time_averaged = self.get_time_list(
                time_elapsed / ( self.kw["number"] if "number" in self.kw else 100 )
            )
            print("{0.__name__}: took {1[0]}:{1[1]}:{1[2]} per loop with {2[0]}:{2[1]}:{2[2]} overall".format(func, run_time_averaged, run_time),
                  file=sys.stderr
                  )
            return val
        return timed_fn