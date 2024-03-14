import caesar
from SubstitutionCipher import SubstitutionCipher


class ChildCaesar(SubstitutionCipher):
    def __init__(self, shift):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        forward = alphabet[shift:] + alphabet[:shift]
        super().__init__(forward)