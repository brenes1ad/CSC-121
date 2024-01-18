"""
stopwatch.py -- timer class to give simple instrumenting capabilities to time
using seconds or nanoseconds

T. Brenes
CS121 W24
1/16/24
Lab2
"""
import time

class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.start_timeNS = 0

    def start(self):
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
        self.start_timeNS = time.perf_counter_ns()

    def stopNS(self):
        st = self.start_timeNS
        curr = time.perf_counter_ns()
        print("time = %d and starttime = %d" %(st, curr))
        print("and their difference is %d" %(curr - st))
        elapsedNS = time.perf_counter_ns() - self.start_timeNS
        self.start_timeNS = 0
        return elapsedNS

    def splitNS(self):
        return time.perf_counter_ns() - self.start_timeNS

def test():
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




if __name__ == "__main__":
    test()
else:
    print("stopwatch's __name__ value: ", __name__)