"""
Main.py -- a testbed for different list initializations that we
instrument with our Stopwatch class

T. Brenes
CSC121 W24
1/16/24
Lab2

Summary: My first take away is that Python can be crazy annoying to debug. We spent probably close to 2 hours
trying to figure out what was wrong with my code just for it to be missing an "NS" at the end of my first
.stopNS() function. If it were a compiled langauge like java, that would have been caught immediately and would
have been a quick fix. In terms of the stopwatch, the speed increases as we go through the different methods. Method
one is the slowest, which makes sense to me because it's adding and iterating 10 million times which just seems
like it would be the slowest. Method two is roughly .01 seconds faster than method one. This one I kind of just have
to believe because I don't fully know how list-comprehension works, I just know how to use it. Method three is by far
the fastest taking only .002 seconds to create the list. This also makes sense to me as it doesn't have to do millions
of iterations, but only one multiplication, which I assume arithmetic operations would already be faster than
iterating.
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
    elapsedNS = timerNS.stopNS()
    print("Method 1: ")
    print(f"It took {elapsedSec} seconds to create list of 10 million zeros using method 1")
    print("It took %d nanoseconds to create list of 10 million zeros using method 1" % elapsedNS)
    print()

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