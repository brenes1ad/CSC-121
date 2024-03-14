"""
CipherTest.py -- testbed for running our encryption tests
Tony Brenes
CSC121 W24
3/12/24
Lab 09
"""
from caesar import CaesarCipher
from SubstitutionCipher import SubstitutionCipher
from RandomCipher import RandomCipher
from childCaesar import ChildCaesar
from random import shuffle

if __name__ == '__main__':
  cipher = CaesarCipher(3)
  message = "THE EAGLE IS IN play; MEET AT JOE'S."
  coded = cipher.encrypt(message)
  print('Secret: ', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)

  myList = list("ABCDEFGabcdefg;'")
  shuffle(myList)
  mystr = "".join(myList)
  print("cipherstring = ", mystr)
  cipher = SubstitutionCipher(mystr)
  message = "THE EAGLE IS a fish-eating bird, man; MEET AT JOE'S."
  coded = cipher.encrypt(message)
  print('Secret: ', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)

  cipher = RandomCipher()
  message = "THE EAGLE IS IN play; MEET AT JOE'S."
  coded = cipher.encrypt(message)
  print('Secret: ', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)

  cipher = ChildCaesar(3)
  message = "THE EAGLE IS IN play; MEET AT JOE'S."
  coded = cipher.encrypt(message)
  print('Secret: ', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)

