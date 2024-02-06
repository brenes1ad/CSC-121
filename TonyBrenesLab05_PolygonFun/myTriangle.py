"""
myTriangle.py -- create a triangle object
"""

from myPolygon import MyPolygon
import graphics as gr

class MyTriangle(MyPolygon):
    """a MyPolygon class to create random triangles"""

    def __init__(self, width=200, height=200):
        """creates a random triangle in a width x height box"""
        self.w = width
        self.h = height

        r = width / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = self.randtheta(0, 120)
        self.a = gr.Point(r * self.cosd(theta) + centerx, r * self.sind(theta) + centery)
        theta = self.randtheta(120, 240)
        self.b = gr.Point(r * self.cosd(theta) + centerx, r * self.sind(theta) + centery)
        theta = self.randtheta(240, 360)
        self.c = gr.Point(r * self.cosd(theta) + centerx, r * self.sind(theta) + centery)

    def area(self):
        return 5

    def peri(self):
        return 5

    def draw(self):
        pass
