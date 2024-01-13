"""
primes.py introducing pycharm and beginning level algorithm coding

This code will print out all prime numbers less than 1000 a modified brute force algorithm
and using order pi(n) secondary storage

Tony Brenes
CSC 121  W24 (Lab L01)
1/9/2024
"""
import math

# task 1: print all prime numbers less than 1000

# BRUTE FORCE
count = 0
primeList = []
for num in range(2, 10001):
    # if num is prime, print, else don't
    prime = True

    for num2 in primeList:
        """if a*b = i, then never have to check for a > sqrt(i)"""
        if num2 > math.sqrt(num):
            break
        count += 1
        if num % num2 == 0:
            prime = False
            break

    if prime:
        primeList.append(num)
        print(num)

print("There are", count, "comparisons")

# task 2: write a function to print out the next prime,
#   starting with 2 primeFun() will print out 2, called again 3, called again 5...

# Task 3: write the Sieve of Eratosthenes

# Task 2 and 3 didn't get finished, but weren't needed for assignment
