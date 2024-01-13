# #Exercise R1
# def isMultiple(n,m):
#     if n % m == 0:
#         return True
#     else:
#         return False
#

# #Exercise R2
# evens = ["2", "4", "6", "8"]
# odds = ["1", "3", "5", "7", "9"]
# def isEven(k):
#     k = str(k)
#     if k[-1] in evens:
#         return True
#     elif k[-1] in odds:
#         return False

# #Exercise R3
# def minmax(data):
#     minValue = data[0]
#     maxValue = data[0]
#     for thing in data:
#         if thing < minValue:
#             minValue = thing
#         if thing > maxValue:
#             maxValue = thing
#     return minValue, maxValue

#Exercise R4
def sumOfSquares(n):
    finalNum = 0
    for thing in range(n):
        finalNum += thing**2
    return finalNum


