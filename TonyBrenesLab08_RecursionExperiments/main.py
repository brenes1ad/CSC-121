"""
main.py -- testing recursion exercises

Tony Brenes
3/5/2024
CSC121 W24
Lab 08
"""

from random import randint
from BetterStopwatch import BetterStopwatch

nsec = BetterStopwatch()
def myQuickSort(A):
    """:param A -- list to be sorted
    :return sorted list"""
    if len(A) == 0:
        return A
    pivot = A[0]
    left = []
    right = []
    for i in range(1, len(A)):
        if A[i] <= pivot:
            left.append(A[i])
        else:
            right.append(A[i])
    return myQuickSort(left) + [pivot] + myQuickSort(right)

print(myQuickSort([7,15,3,56,17,2,7,44,843,3]))

for i in range(1000, 40001, 1000):
    a1 = [randint(1,1000) for k in range(i)]
    a2 = list(a1)

    nsec.startNS()
    a1 = sorted(a1)
    tTimSort = nsec.stopNS()
   # print("built-in sort of %d elements took %d nsec" % (i, tTimSort))

    nsec.startNS()
    a2 = myQuickSort(a2)
    tQSort = nsec.stopNS()
   # print("myQuickSort sort of %d elements took %d nsec" % (i, nsec.stopNS()))
    print("size %d, ratio %f" % (i, (tQSort / tTimSort)))
print("")

#Towers of Hanoi
print("Towers of Hanoi")
print("")
def towerSolver(numDisks, src, dst, helper):
    if numDisks > 0:
        towerSolver(numDisks - 1, src, helper, dst)
        print(f"move disk {numDisks} from peg {src} to peg {dst}")
        towerSolver(numDisks - 1, helper, dst, src)
    else:
        pass


towerSolver(3, 1, 3, 2)
