"""
testPolygonsMain.py -- gives menu to choose a shape object, draws the shape, and prints area and perimeter

Tony Brenes
CSC121 W24
1/6/24
Lab 5
"""

import graphics as gr
import myPolygon
from myTriangle import *
from myQuadrilateral import *


shapes = [MyRectangle, MyQuadrilateral, MySquare, MyTriangle, MyEquilTriangle, MyIsos]
shapeNames = []


while True:
    for shape in shapes:
        shapeNames.append(shape.__name__.lower())
        print(shape.__name__)
    a = input("Enter shape class name to create the shape(enter empty string to quit: ")
    if a.lower() not in shapeNames and a != "":
        print("Invalid shape. Try again \n")
    for x in shapes:
        if a.lower() == x.__name__.lower():
            b = x()
            print(f"Area: {b.area()}")
            print(f"Perimeter: {b.peri()}")
            b.draw()
            print("")
    if a == "":
        break






