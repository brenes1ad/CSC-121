"""
myQuadrilateral.py -- Create quadrilateral object and subclass of quadrilateral class
"""

from myPolygon import MyPolygon
import graphics as gr
from helperFunctions import *

class MyQuadrilateral(MyPolygon):
    def __init__(self, width=200, height=200):
        """creates a random quadrilateral in a width x height box"""
        self.w = width
        self.h = height

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = randtheta(0, 90)
        self.a = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        theta = randtheta(90, 180)
        self.b = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        theta = randtheta(180, 270)
        self.c = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)
        theta = randtheta(270, 360)
        self.d = gr.Point(r * cosd(theta) + centerx, r * sind(theta) + centery)

    def draw(self):
        win = gr.GraphWin("Quadrilateral", self.w, self.h)
        c = gr.Polygon(self.a, self.b, self.c, self.d)
        c.draw(win)
        win.getMouse()
        win.close()

    def area(self):
        return triArea(self.a, self.b, self.c) + triArea(self.a, self.c, self.d)

    def peri(self):
        return ((distBetweenPoints(self.a, self.b)) + (distBetweenPoints(self.b, self.c))
                + (distBetweenPoints(self.c, self.d))
                + (distBetweenPoints(self.d, self.a)))

class MyRectangle(MyQuadrilateral):
    def __init__(self, width=200, height=200):
        self.w = width
        self.h = height

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2

        theta1 = randtheta(0,180)
        self.a = gr.Point(r * cosd(theta1) + centerx, r * sind(theta1) + centery)
        theta2 = randtheta(theta1, theta1 + 180)
        self.b =gr.Point(r * cosd(theta2) + centerx, r * sind(theta2) + centery)
        self.c = gr.Point(r * cosd(theta1 + 180) + centerx, r * sind(theta1 + 180) + centery)
        self.d = gr.Point(r * cosd(theta2 + 180) + centerx, r * sind(theta2 + 180) + centery)

class MySquare(MyQuadrilateral):
    def __init__(self, width = 200, height = 200):
        self.w = width
        self.h = height

        r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2

        theta1 = randtheta(0, 180)
        self.a = gr.Point(r * cosd(theta1) + centerx, r * sind(theta1) + centery)
        self.b = gr.Point(r * cosd(theta1 + 90) + centerx, r * sind(theta1 + 90) + centery)
        self.c = gr.Point(r * cosd(theta1 + 180) + centerx, r * sind(theta1 + 180) + centery)
        self.d = gr.Point(r * cosd(theta1 + 270) + centerx, r * sind(theta1 + 270) + centery)



