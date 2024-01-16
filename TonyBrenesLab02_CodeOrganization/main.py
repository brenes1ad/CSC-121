"""
Main.py -- a testbed for different list initializations that we
instrument with our Stopwatch class

T. Brenes
CSC121 W24
1/16/24
Lab2
"""

"""list_tests() -- try three different ways to make a list of 10_000_000 zeros"""
def mainListTests(n):
    # Method 1
    nums = []
    for i in range(n):
        nums.append(0)


if __name__ == "__main__":
    mainListTests(10_000_000)