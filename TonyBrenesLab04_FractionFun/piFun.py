"""
piFun.py -- use the rational function code to compute pi using various series

Tony Brenes
CSC121 W24
1/30/24

Leibniz/Gregory Formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 ...
Let's try e instead, using Euler's formula e =sum_i=0^inf 1/(over) i!(factorial)
    -1 over zero factorial + 1  over 1 Factorial + 1 over 2 factorial ...
"""

from rationals import Fraction as Frac
import rationals
import math

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

# Let's use Leibniz/Gregory and our fractions to compute pi
piOver4 = Frac.ZERO
numTermsPi = 1000
numTermsE = 18
for i in range(numTermsPi):
    piOver4 = piOver4 + Frac((-1)**i, 2*i + 1)

piFrac = piOver4 * Frac(4)
print("piFrac = ", piFrac)
piFloat = float(piFrac)
print("Computed pi =  ", piFloat)
print("compared to math.pi = ", math.pi)
print("with an absolute error of ", math.fabs(piFloat - math.pi))
print("with a relative error of", math.fabs(piFloat - math.pi) / math.pi)


# Now do other pi formula. Remember to take sqrt and then multiply by 6
"""Let's try a different one: pi**2 /(over) 6 = sum_k = 1^inf 1 /(over) k^2
    For value of pi: take square root and then multiply by 6
    - 1 over 1 squared + 1 over 2 squared + 1 over 3 squared"""
print("")
piSqrtOver6 = Frac.ZERO
for i in range(1, numTermsPi):
    piSqrtOver6 = piSqrtOver6 + Frac(1, i**2)
piSqrOver6Float = float(piSqrtOver6)
piFloat = (piSqrOver6Float * 6) ** 0.5
print(f"Method 2 pi calculated to be: {piFloat}")


# Now do Euler's e formula
"""Let's try e instead, using Euler's formula e =sum_i=0^inf 1/(over) i!(factorial)
    -1 over zero factorial + 1  over 1 Factorial + 1 over 2 factorial ..."""
print("")
calculatedE = Frac.ZERO
for i in range(0, numTermsE):
    calculatedE = calculatedE + Frac(1, int(factorial(i)))
print(f"Calculted e: {float(calculatedE)}")
print(f"Real e: {math.e}")
print(f"error{float(calculatedE) - math.e}")

"""It is impossible to converge to 5 decimal points of accuracy for either pi
calculation because you get a string length limit.
It takes 18 iterations to get a a full convergence to e"""






