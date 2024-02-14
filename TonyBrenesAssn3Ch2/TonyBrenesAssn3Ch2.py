"""
TonyBrenesAssn3Ch2.py
Tony Brenes
CSC121 W24
1/29/24

All coding problems were written and tested in seperate file then copy and pasting here
"""

#R1
#Medical Machines, plane's autopilot, car safety systems

#R2
#New products being added and old ones being removed as what people buy change

#R3

#R4
class Flower():
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def setName(self, name):
        self._name = name
    def setPetals(self, petals):
        self._petals = petals
    def setPrice(self, price):
        self._price = price

    def getName(self):
        return self._name
    def getPetals(self):
        return self._petals
    def getPrice(self):
        return self._price

#R5
def charge(self, price):
    if not isinstance(price, (float, int)):
        raise TypeError("Price must be a number")
    if price + self._balance > self._limit:
        return False
    else:
        self._balance += price
    return True

#R6
def charge(self, price):
    if not isinstance(price, (float, int)):
        raise TypeError("Price must be a number")
    if price < 0:
        raise ValueError("Price can't be negative")
    if price + self._balance > self._limit:
        return False
    else:
        self._balance += price
    return True

#R7
def __init__ (self, cutsomer, bank, acnt, limit, balance=0):
    self.cutsomer = cutsomer
    self.bank = bank
    self.acnt = acnt
    self.limit = limit
    self.balance = balance

#R8
# for val in range(1, 59):
#Card 3 is the first to go over

#R9
def __sub__(self, other):
    if len(self) != len(other):
        raise ValueError("Length mismatch")
    result = Vector(len(self))
    for thing in range (len(self)):
        result[thing] = self[thing] - other[thing]
    return result

#R10
def __neg__(self):
    for i in range (len(self)):
        self[i] = self[i] * -1
    return self

#R11
"""
I really don't know. In lab, we mentioned needed a rmul() for fraction so maybe
there's a radd thing that we would need for these vectors"""

#R12
def __mul__(self, n):
    for i in range (len(self)):
        self[i] = n * self[i]
    return self

#R13
def __rmul__(self, n):
    for thing in range(len(self)):
        self[thing] = self[thing] * n
    return self

#R14
def __mul__(self, other):
    if len(self) != len(other):
        raise ValueError("Mismatching dimensions")
    dotProduct = 0
    for i in range(len(self)):
        dotProduct = dotProduct + (self[i] * other[i])
    return dotProduct

#R15
def __init__(self, d, listToVec=None):
    if isinstance(d, int):
        self.coords = [0] * d
    else:
        self.coords = list(listToVec)

#R16

#R17
#Submitted as pdf

#R18
# thing = FibonacciProgression(2,2)
# for i in range(7)
#     thing.advance()

#R19
#7.205759404E16

#R20

#R21

#R22
def __eq__(self, other):
    if len(self) != len(other):
        return False
    for i in range(len(self)):
        if self[i] != other[i]:
            return False
    return True

#R23
def __lt__(self, other):
    if len(self) < len(other):
        for i in range(len(self)):
            if self[i] > other[i]:
                return False
            if self[i] < other[i]:
                return True
        return True
    elif len(other) <= len(self):
        for i in range(len(other)):
            if self[i] > other[i]:
                return False
            if self[i] < other[i]:
                return True
        return False
