"""
myPolygon.py -- an abstract base class for creating and drawing random polygons.

Tony Brenes
CSC121 W24
2/6/24
"""

from abc import ABCMeta, abstractmethod

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

