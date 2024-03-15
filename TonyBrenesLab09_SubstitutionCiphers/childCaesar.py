"""
ChildCaesar.py -- Subclass of SubstitutionCipher that acts as a caesar cipher

Tony Brenes
CSC121 W24
3/14/24
Lab 09
"""

from SubstitutionCipher import SubstitutionCipher


class ChildCaesar(SubstitutionCipher):
    def __init__(self, shift):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        forward = alphabet[shift:] + alphabet[:shift]
        super().__init__(forward)