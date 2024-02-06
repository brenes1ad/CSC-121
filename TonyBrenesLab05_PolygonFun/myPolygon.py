"""
myPolygon.py -- an abstract base class for creating and drawing random polygons.
Tony Brenes
CSC121 W24
2/6/24
"""

from abc import ABCMeta, abstractmethod
from math import sin, cos, pi
from random import random



class MyPolygon(metaclass=ABCMeta):
    """Our abstract base class for creating renderable polygons"""
    @abstractmethod
    def area(self):
        """returns the area of the polygon"""

    @abstractmethod
    def peri(self):
        """returns the perimeter of the polygon"""

    @abstractmethod
    def draw(self):
        """opens graphics.py window, draw the polygon, and wait for
        mouseclick before returning"""

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