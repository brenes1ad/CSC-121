"""
testPolygonsMain.py -- test the polygon code
"""

import graphics as gr
import myPolygon
from myTriangle import *
from myQuadrilateral import *


print("Triangle:")
triangle = MyTriangle()
print(f"perimeter: {triangle.peri()}")
print(f"area: {triangle.area()}")
triangle.draw()


print(" \n Quadrilateral:")
quad = MyQuadrilateral()
print(f"perimeter: {quad.peri()}")
print(f"area: {quad.area()}")
quad.draw()







