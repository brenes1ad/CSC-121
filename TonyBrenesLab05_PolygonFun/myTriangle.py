"""
myTriangle.py -- create a triangle object
"""

from myPolygon import MyPolygon
import graphics as gr
from helperFunctions import *


class MyTriangle(MyPolygon):

    from helperFunctions import randtheta, cosd, sind

    """a MyPolygon class to create random triangles"""


    def __init__(self, width=200, height=200):
        """creates a random triangle in a width x height box"""
        self.w = width
        self.h = height

        self.r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = randtheta(0, 120)
        self.a = gr.Point(self.r * cosd(theta) + centerx, self.r * sind(theta) + centery)
        theta = randtheta(120, 240)
        self.b = gr.Point(self.r * cosd(theta) + centerx, self.r * sind(theta) + centery)
        theta = randtheta(240, 360)
        self.c = gr.Point(self.r * cosd(theta) + centerx, self.r * sind(theta) + centery)

    def area(self):
        return triArea(self.a, self.b, self.c)

    def peri(self):
        return distBetweenPoints(self.a, self.b) + distBetweenPoints(self.b, self.c) + distBetweenPoints(self.c, self.a)

    def draw(self):
        win = gr.GraphWin("Triangle", self.w, self.h)
        c = gr.Polygon(self.a, self.b, self.c)
        c.draw(win)
        win.getMouse()
        win.close()

