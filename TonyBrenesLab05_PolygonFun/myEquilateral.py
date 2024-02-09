"""
myEquilateral.py -- Child class of myTriangle to create an equilateral triangle
"""
from myTriangle import MyTriangle
import graphics as gr
from helperFunctions import *
class MyEquilTriangle(MyTriangle):
    def __init__(self, width=200, height=200):

        self.w = width
        self.h = height

        self.r = self.w / 2
        centerx = self.w / 2
        centery = self.h / 2
        theta = randtheta(0,120)
