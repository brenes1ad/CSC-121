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


class BetterStopwatch:

    def __init__(self):
        self.start_time = 0
        self.start_timeNS = 0
        self.secondsTimerRunning = False
        self.NSTimerRunning = False

    def start(self):
        self.secondsTimerRunning = True
        self.start_time = time.perf_counter()

    def stop(self):
        """
        get elapsed time in fractional seconds and reset to zero
        :return: (float) seconds
        """
        if self.secondsTimerRunning == False and self.NSTimerRunning == True:
            raise StartStopMismatchError()

        elapsed = time.perf_counter() - self.start_time
        self.start_time = 0
        self.secondsTimerRunning = False

        return elapsed

    def split(self):
        """
        get elapsed time as above but don't reset time
        :return: (float) seconds
        """
        if self.secondsTimerRunning == False and self.NSTimerRunning == True:
            raise StartStopMismatchError()
        return time.perf_counter() - self.start_time

    def startNS(self):
        self.NSTimerRunning = True
        self.start_timeNS = time.perf_counter_ns()

    def stopNS(self):
        if self.secondsTimerRunning == True and self.NSTimerRunning == False:
            raise StartStopMismatchError()
        curr = time.perf_counter_ns()
        elapsedNS = time.perf_counter_ns() - self.start_timeNS
        self.start_timeNS = 0
        self.NSTimerRunning = False
        return elapsedNS

    def splitNS(self):
        if self.secondsTimerRunning == True and self.NSTimerRunning == False:
            raise StartStopMismatchError()
        return time.perf_counter_ns() - self.start_timeNS


def _test():
    print("Stopwatch tests")
    timer = BetterStopwatch()
    timerNS = BetterStopwatch()
    timer.start()
    timerNS.startNS()
    for i in range(10_000_000):
        pass
    elapsed = timer.stop()
    elapsedNS = timerNS.stopNS()
    print("elapsed time =", elapsed)
    print("NS TIme", elapsedNS)


try:
    timer = BetterStopwatch()
    timer.startNS()
    timer.stop()

except StartStopMismatchError:
    print("Mismatch detected, exception raised")

