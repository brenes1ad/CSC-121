"""
Main.py -- a testbed for different list initializations that we
instrument with our Stopwatch class

T. Brenes
CSC121 W24
1/16/24
Lab2
"""
import stopwatch



"""
list_tests() -- try three different ways to make a list of 10_000_000 zeros
"""
def mainListTests(n):
    timerSec = stopwatch.Stopwatch()
    timerNS = stopwatch.Stopwatch()

    # Method 1 -- using a for-loops
    nums = []
    timerSec.start()
    timerNS.startNS()
    for i in range(n):
        nums.append(0)
    elapsedSec = timerSec.stop()
    elapsedNS = timerNS.stop()
    print("It took", elapsedSec, "seconds to create list of 10 million zeros using method 1")
    print("It took %d nanoseconds to create list of 10 million zeros using method 1" % elapsedNS)
    print()

    # Method 2 -- using a list-comprehension
    nums = [0 for i in range(n)]

    # Method 3 -- built in lists-multiplier
    timerNS.startNS()
    nums = [0] * n
    elapsed = timerNS.stopNS()
    print("It took %d nanoseconds to create list of 10 million zeros using method 3" % elapsed)


if __name__ == "__main__":
    mainListTests(10_000_00)