"""
PolygonTestDisplay.py -- test the display of polygons and drawing using graphics.py
A. Thall
CSC121 W24
Lab 5
Documentation for graphics.py v5 can be found at:
https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

2/6/24
"""
import graphics as gr
from math import sin, cos, pi
from random import random

def randtheta(a, b):
    """Return a random value in an interval [a, b)
       --we'll use this to get random angles for points on a circle
    :param a: lower bound, inclusive
    :param b: upper bound, exclusive
    :return: float r in [a, b), excluding upper bound
    """
    theta = random()*(b - a) + a
    print(theta)
    return theta

def cosd(deg):
    """compute cosine given angle in degrees, not radians"""
    return cos(2*pi*deg/360)

def sind(deg):
    """compute sine given angle in degrees, not radians"""
    return sin(2*pi*deg/360)

def main():
    win = gr.GraphWin("Draw Shapes!", 200, 200)
    c = gr.Circle(gr.Point(50,50), 10)
    c.draw(win)
    win.getMouse() # Pause to view result
    c.undraw()

    c = gr.Rectangle(gr.Point(50, 50), gr.Point(150, 150))
    c.draw(win)
    win.getMouse()  # Pause to view result
    c.undraw()

    radius = 50
    centerx = 100
    centery = 100
    theta = randtheta(0, 90)
    a = gr.Point(50*cosd(theta) + centerx, 50*sind(theta) + centery)
    theta = randtheta(90, 180)
    b = gr.Point(50*cosd(theta) + centerx, 50*sind(theta) + centery)
    theta = randtheta(180, 270)
    c = gr.Point(50*cosd(theta) + centerx, 50*sind(theta) + centery)
    theta = randtheta(270, 360)
    d = gr.Point(50*cosd(theta) + centerx, 50*sind(theta) + centery)

    c = gr.Polygon(a, b, c, d)
    c.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done
main()