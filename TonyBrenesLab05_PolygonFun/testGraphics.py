"""
testGraphics.py -- testing graphics.py, Zelle's module for simple display
Tony Brenes
CSC121 W24
2/6/24
"""

import graphics as gr

def main():
    win = gr.GraphWin("My Circle", 100, 100)
    c = gr.Circle(gr.Point(50,50), 10)
    c.draw(win)
    win.getMouse()
    win.close()

main()