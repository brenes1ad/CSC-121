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
    timerNS.startNS()
    timerSec.start()
    for i in range(n):
        nums.append(0)
    elapsedNS = timerNS.stop()
    elapsedSec = timerSec.stop()
    print("Method 1: ")
    print("It took %f seconds to create list of 10 million zeros using method 1" % elapsedSec)
    print("It took %d nanoseconds to create list of 10 million zeros using method 1" % elapsedNS, "\n")


    # Method 2 -- using a list-comprehension
    timerNS.startNS()
    timerSec.start()
    nums = [0 for i in range(n)]
    elapsedNS = timerNS.stopNS()
    elapsedSec = timerSec.stop()
    print("Method 2: ")
    print("It took %f seconds to create list of 10 million zeros using method 2" % elapsedSec)
    print("It took %d nanoseconds to create list of 10 million zeros using method 2" % elapsedNS, "\n")

    # Method 3 -- built in lists-multiplier
    timerNS.startNS()
    timerSec.start()
    nums = [0] * n
    elapsedNS = timerNS.stopNS()
    elapsedSec = timerSec.stop()
    print("Method 3: ")
    print("It took %f seconds to create list of 10 million zeros using method 3" % elapsedSec)
    print("It took %d nanoseconds to create list of 10 million zeros using method 3" % elapsedNS)


if __name__ == "__main__":
    mainListTests(10_000_00)