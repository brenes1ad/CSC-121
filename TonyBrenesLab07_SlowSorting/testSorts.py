"""
testSorts.py -- run asymptotic time trials on our three sorts

Tony Brenes
CSC121 W24
2/20/24
Lab 7
"""

from asympPrintout import asympPrintout
from slow_sorts import selection_sort, insertion_sort, bubble_sort
from random import randint

"""[(n, t), (n, t), (n, t), ... ] for averages of each sort"""
selectTrials = []
insertTrials = []
bubbleTrials = []

sizes =[100, 200, 300, 500, 1000, 2000]
numTrials = 30
for n in sizes:
    comps1 = 0
    comps2 = 0
    swaps3 = 0
    for trial in range(numTrials):
        arr1 = [randint(0, n * 10) for i in range(n)]
        arr2 = list(arr1)
        arr3 = list(arr1)
        comps1 += selection_sort(arr1)
        comps2 += insertion_sort(arr2)
        swaps3 += bubble_sort(arr3)
    comps1 /= numTrials
    comps2 /= numTrials
    swaps3 /= numTrials
    selectTrials.append((n, comps1))
    insertTrials.append((n, comps2))
    bubbleTrials.append((n, swaps3))
print("Selection Sort")
asympPrintout(selectTrials)
print("")
print("Insertion Sort")
asympPrintout(insertTrials)
print("")
print("Bubble Sort")
asympPrintout(bubbleTrials)

