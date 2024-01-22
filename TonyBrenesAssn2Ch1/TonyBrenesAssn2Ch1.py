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

#R10
#for thing in range(8,-10,-2):

#R11
doubles = [2**k for k in range(9)]

#R12
import random
from random import randrange
def randrangeAsChoice(list):
    randIndex = randrange(len(list))
    return list[randIndex]

#C13
"""Iterate through the list with a for loop in range of the length of the list. You'd start
at negative one and decrease your i value by one each step to go through the list backwards.
You'd then append those values to a new list, therefore reversing the list."""
"""The main difference between how I would have done it and how the reverse() method works is the built-
in method doesn't append to a new list, it updates the same list you attached to the funciton but reversed"""

#C14
def hasOddProductPair(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] * list[j]) % 2 == 1:
                return True

    return False

#C15
def distinctNumbers(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return False
    return True

#C16

#C17

#C18
increasingAdd = [k * (k-1) for k in range(1,11,)]

#C19
letters = [chr(char).lower() for char in range(65, 91)]

#C20

#C21
def reverseAfterError():
    list= []
    while True:
        try:
            list.append(input("Enter something: "))
        except EOFError:
            list.reverse()
            break
    return list

#C22

#C23
list = [0,1,2,3]
try:
    list[12] = 1
except IndexError:
    print("Don't try buffer overflow attacks in python")

#C24
def countVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in str:
        if letter in vowels:
            count += 1
    return count

#C25
def removePunctuation(str):
    """
    I know there are more punctuation marks, but I chose the most used
    and it seemed like a hastle to include them all
    """
    punctionation = [',', '.', '!', '?', "\'", ':', ';', "\""]
    returnSentence = ""
    for char in str:
        if char not in punctionation:
            returnSentence += char
    return returnSentence
