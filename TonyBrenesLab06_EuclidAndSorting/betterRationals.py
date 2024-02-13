"""
rationals.py
Some test code for rational numbers
A. Thall
CSC 121 W24
1/28/24
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
class Fraction:
    def __init__(self, a, b=1):
        """
        :param a:
        :param b:
        Create a fraction object:
        If b not given, make denom 1.
        If b == 0, raise ZeroDivisionError
        If isinstance(a, int) is false, or likewise b, raise TypeError
        Otherwise set num and denom to a and b respectively
        """
        if b == 0:
            raise ZeroDivisionError("Denominator cannon be Zero")
        if isinstance(a, int) is False or isinstance(b, int) is False:
            raise TypeError("Numerator and Denominator must be integers")
        q = gcd(a, b)
        self.num = a // q
        self.denom = b // q

    def __add__(self, other):
        """
        :param other: Fraction to add to self.  What if it's not a Fraction?
        :return: new Fraction as sum of two fractions.  How?
        """
        if self.denom == other.denom:
            newNum = self.num + other.num
            newDenom = self.denom
        else:
            commonNum1 = self.num * other.denom
            commonDenom = self.denom * other.denom
            commonNum2 = other.num * self.denom
            newNum = commonNum1 + commonNum2
            newDenom = commonDenom

        return Fraction(newNum, newDenom)

    def __mul__(self, other):
        """
        :param other:
        :return: new Fraction as product of self and other
        """
        newNum = self.num * other.num
        newDenom = self.denom * other.denom

        return Fraction(newNum, newDenom)

    def __rmul__(self, other):
        return Fraction(0,1)

    def __eq__(self, other):
        """
        overload == operator to compare two Fractions.
        What if comparing to an int or float?
        :param other:
        :return: true if have same quotient value, else False
        """
        return self.num * other.denom == self.denom * other.num

    def __str__(self):
        """
        overload string cast
        :return: "Fraction(a, b)", where a and b are self.num and denom
        """

        return f"Fraction({self.num}, {self.denom})"

    def __float__(self):
        """
        overload float cast by dividing self.num by self.denom,
        allowing float(val) for Fraction val
        :return: float value of quotient
        """
        return self.num / self.denom

    def __int__(self):
        """
        overload int cast by dividing self.num by self.denom,
        allowing float(val) for Fraction val
        :return: int value of quotient
        """
        return self.num // self.denom

Fraction.ZERO = Fraction(0, 1)
Fraction.ONE = Fraction(1, 1)

def _test():
    a = Fraction(25, 27)
    print("fraction a = ", a)
    b = Fraction(2, 27)
    print("fraction b = ", b)
    c = a + b
    print("a + b = ", c)
    c = a*b
    print("a*b = ", c)
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    print(a, "==", b, "is ", a == b)
    b = Fraction(2, 3)
    print(a, "==", b, "is ", a == b)
    try:
        a = Fraction(5, 0)
        print("hmm, seems to allow", a)
    except ZeroDivisionError:
        print("hah!  caught that error, 5/0 is illegal")
    try:
        a = Fraction(5.5, 1)
        print("hmm, seems to allow: ", a)
    except TypeError as e:
        print("hah!  caught that: ", e)
    a = Fraction(5)
    print("Default value a=5 b missing: ", a)



if __name__ == "__main__":
    _test()