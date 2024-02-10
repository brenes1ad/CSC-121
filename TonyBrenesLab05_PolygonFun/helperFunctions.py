"""
helperFunctions.py -- needed calculation functions for other classes
"""

from random import random
from math import sin, cos, pi, sqrt, hypot
import graphics as gr

def randtheta(a, b):
    """Return a random value in an interval [a, b)
       --we'll use this to get random angles for points on a circle
    :param a: lower bound, inclusive
    :param b: upper bound, exclusive
    :return: float r in [a, b), excluding upper bound
    """
    theta = random() * (b - a) + a
    print(theta)
    return theta


def cosd(deg):
    """compute cosine given angle in degrees, not radians"""
    return cos(2 * pi * deg / 360)


def sind(deg):
    """compute sine given angle in degrees, not radians"""
    return sin(2 * pi * deg / 360)

def distBetweenPoints(a, b):
    x1, y1 = a.getX(), a.getY()
    x2, y2 = b.getX(), b.getY()
    return hypot(x2 - x1, y2 - y1)

def triArea(a, b, c):
    aDist = distBetweenPoints(a, b)
    bDist = distBetweenPoints(b, c)
    cDist = distBetweenPoints(c, a)
    s = (aDist + bDist + cDist) / 2
    return sqrt(s*(s - aDist)*(s - bDist)*(s - cDist))




