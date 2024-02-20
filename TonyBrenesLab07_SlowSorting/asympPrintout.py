"""
asympPrintout.py -- automatically creates and prints tabulated data

Tony Brenes
CSC121 W24
2/20/24
Lab 6
"""
"""
asymp_printout.py -- given a list of values [(n1, Tn1), (n2, Tn2), ... ]
    print out a function table:
   "n     T    T/log(n)   T/sqrt(n)   T/n   T/(n*log(n))  T/n**2"
    n1    Tn1      ...         ...    ...
    n2    Tn2      ...
"""

from math import sqrt, log2

def asympPrintout(sizeCountList):
    sizeCountList.sort()
    print("%7s %12s %12s %12s %12s %12s %12s" % ("n", "T", "T/log(n)",
                                                "T/sqrt(n)", "T/n", "T/(n*log(n))", "T/n**2"))
    for n, tn in sizeCountList:
        print("%7d %12f %12f %12f %12f %12f %12f" % (n, tn, tn/log2(n),
                                                    tn/sqrt(n), tn/n, tn/(n*log2(n)), tn/n**2))


