"""
testPolygonsMain.py -- test the polygon code
"""

import graphics as gr
import myPolygon
from TonyBrenesLab05_PolygonFun import myQuadrilateral
from myTriangle import *
from myQuadrilateral import *


shapes = [MyRectangle, MyQuadrilateral, MySquare, MyTriangle, MyEquilTriangle, MyIsos]
shapeNames = []


while True:
    for shape in shapes:
        shapeNames.append(shape.__name__)
        print(shape.__name__)
    a = input("Enter shape class name(enter empty string to quit: ")
    if a not in shapeNames and a != "":
        print("Invalid shape. Try again \n")
    for x in shapes:
        if a.lower() == x.__name__.lower():
            b = x()
            b.draw()
            print("")
    if a == "":
        break






