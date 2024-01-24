"""
stopwatch.py -- timer class to give simple instrumenting capabilities to time
using seconds or nanoseconds

T. Brenes
CS121 W24
1/16/24
Lab2
"""

#Need to implement boolean to throw error when mismatching start
#and stop timer
import time


class StartStopMismatchError(Exception):
    pass


class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.start_timeNS = 0

    def start(self):
        self.secondsTimer = True
        self.start_time = time.perf_counter()

    def stop(self):
        """
        get elapsed time in fractional seconds and reset to zero
        :return: (float) seconds
        """

        elapsed = time.perf_counter() - self.start_time
        self.start_time = 0
        return elapsed

    def split(self):
        """
        get elapsed time as above but don't reset time
        :return: (float) seconds
        """
        return time.perf_counter() - self.start_time

    def startNS(self):
        self.secondTimer = False
        self.start_timeNS = time.perf_counter_ns()

    def stopNS(self):
        st = self.start_timeNS
        curr = time.perf_counter_ns()
        elapsedNS = time.perf_counter_ns() - self.start_timeNS
        self.start_timeNS = 0
        return elapsedNS

    def splitNS(self):
        return time.perf_counter_ns() - self.start_timeNS


def _test():
    print("Stopwatch tests")
    timer = Stopwatch()
    timerNS = Stopwatch()
    timer.start()
    timerNS.startNS()
    for i in range(10_000_000):
        pass
    elapsed = timer.stop()
    elapsedNS = timerNS.stopNS()
    print("elapsed time =", elapsed)
    print("NS TIme", elapsedNS)


try:
    timer = Stopwatch()
    timer.start()
    timer.stopNS()
    print("Exception Error not thrown! Error!")
except StartStopMismatchError:
    print("Mismatch detected, exception raised")

if __name__ == "__main__":
    _test()
else:
    print("stopwatch's __name__ value: ", __name__)