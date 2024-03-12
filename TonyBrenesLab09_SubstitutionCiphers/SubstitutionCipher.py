"""
SubstitutionCipher.py -- parent class for a few different subst. ciphers
Basic form just takes encrypting permutation of alphabet

Tony Brenes
CSC121 W24
3/12/24
Lab 09
"""

class SubstitutionCipher:

    def __init__(self, encodeStr):
        self._forward = encodeStr
        self._alphabet = "".join(sorted(list(encodeStr)))

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self._alphabet, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._forward, self._alphabet)

    def _transform(self, original, from_code, to_code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k] in self._alphabet:
                j = from_code.index(msg[k])  # index from 0 to 25
                msg[k] = to_code[j]  # replace this character
        return ''.join(msg)