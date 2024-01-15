"""
TonyBrenesAssn2Ch1.py

Tony Brenes

CSC121 W24

1/13/24
"""

#R1
def isMultiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

#R2
evens = ["2", "4", "6", "8"]
odds = ["1", "3", "5", "7", "9"]
def isEven(k):
    k = str(k)
    if k[-1] in evens:
        return True
    elif k[-1] in odds:
        return False

#R3
def minmax(data):
    minValue = data[0]
    maxValue = data[0]
    for thing in data:
        if thing < minValue:
            minValue = thing
        if thing > maxValue:
            maxValue = thing
    return minValue, maxValue

#R4
def sumOfSquares(n):
    finalNum = 0
    for thing in range(n):
        finalNum += thing**2
    return finalNum

#R5
def shortSumOfSquares(n):
    return sum(k**2 for k in range(n))

#R6
def oddSumOfSquares(n):
    finalNum = 0
    for thing in range(n):
        if thing % 2 != 0:
            finalNum += thing**2
    return finalNum

#R7
def shortOddSumOfSquares(n):
    return sum(n**2 for n in range(n) if n % 2 != 0)

#R8
# j = n + k
#I don't fully understand this

#R9
# for thing in range(50,90,10):