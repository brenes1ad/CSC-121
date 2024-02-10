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
        + (distBetweenPoints(self.c, self.d)))
        + (distBetweenPoints(self.d, self.a))


quad = MyQuadrilateral()
quad.draw()
print(f"peri: {quad.peri()}")
print(f"area: {quad.area()}")