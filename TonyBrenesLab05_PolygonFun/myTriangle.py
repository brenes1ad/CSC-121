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

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = randtheta(0, 120)
        self.a = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        theta = randtheta(120, 240)
        self.b = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        theta = randtheta(240, 360)
        self.c = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)

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

class MyEquilTriangle(MyTriangle):
    def __init__(self, width=200, height=200):

        self.w = width
        self.h = height

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = randtheta(0,120)

        self.a = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        self.b = gr.Point(r * cosd(theta + 120) + centerx, r * sind(theta + 120) + centery)
        self.c = gr.Point(r * cosd(theta + 240) + centerx, r * sind(theta + 240) + centery)


class MyIsos(MyTriangle):
    def __init__(self, width=200, height=200):

        self.w = width
        self.h = height

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta1 = randtheta(0,360)
        theta2 = randtheta(0,180)

        self.a = gr.Point(r * cosd(theta1) + centerx, r * sind(theta1) + centery)
        self.b = gr.Point(r * cosd(theta1 + theta2) + centerx, r * sind(theta1 + theta2) + centery)
        self.c = gr.Point(r * cosd(theta1 + 2*theta2) + centerx, r * sind(theta1 + 2*theta2) + centery)




