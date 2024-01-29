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