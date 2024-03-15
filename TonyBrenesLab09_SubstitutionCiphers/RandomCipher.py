"""
RandomCipher.py -- subclass of SubstitutionCipher that uses a randomized order of the alphabet, upper and lower,
and digits as the encode string.

Tony Brenes
CSC121 W24
3/14/24
Lab09
"""

import string

from SubstitutionCipher import SubstitutionCipher
from random import randint, shuffle

class RandomCipher(SubstitutionCipher):
    def __init__(self):
        alpha = string.ascii_lowercase + string.ascii_uppercase + string.digits
        alphaList = list(alpha)
        shuffle(alphaList)
        forward = "".join(alphaList)
        super().__init__(forward)
