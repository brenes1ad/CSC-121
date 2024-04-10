"""
gameTree.py -- parent class for our query trees

Tony Brenes
CSC121 W24
4/2/2024
"""

class GameTree:
    def __init__(self, question, ynode=None, nnode=None):
        self.question = question
        self.yesNode = ynode
        self.noNode = nnode

    def play(self):
        return self