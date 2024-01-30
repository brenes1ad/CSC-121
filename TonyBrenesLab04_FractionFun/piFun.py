"""
piFun.py -- use the rational function code to compute pi using various series

Tony Brenes
CSC121 W24
1/30/24

Leibniz/Gregory Formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 ...
Let's try a different one: pi**2 /(over) 6 = sum_k = 1^inf 1 /(over) k^2
    For value of pi: take square root and then multiply by 6
    - 1 over 1 squared + 1 over 2 squared + 1 over 3 squared
Let's try e instead, using Euler's formula e =sum_i=0^inf 1/(over) i!(factorial)
    -1 over zero factorial + 1  over 1 Factorial + 1 over 2 factorial ...
"""

from rationals import Fraction as Frac
import rationals
import math

# Let's use Leibniz/Gregory and our fractions to compute pi
piOver4 = Frac.ZERO
numTerms = 1000
for i in range(numTerms):
    piOver4 = piOver4 + Frac((-1)**i, 2*i + 1)

piFrac = piOver4 * Frac(4)
print("piFrac = ", piFrac)
piFloat = float(piFrac)
print("Computed pi =  ", piFloat)
print("compared to math.pi = ", math.pi)
print("with an absolute error of ", math.fabs(piFloat - math.pi))
print("with a relative error of", math.fabs(piFloat - math.pi) / math.pi)


# Now do other pi formula. Remember to take sqrt and then multiply by 6



# Now do Euler's e formula

# Need factorials
def factorial(n):
    f = 1.0
    for i in range(1, n + 1):
        f *= i
    return f

def factorialB(n):
    if n == 0:
        return 1
    return n * factorialB(n-1)


