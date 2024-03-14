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
