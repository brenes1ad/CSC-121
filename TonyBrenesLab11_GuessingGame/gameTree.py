"""
gameTree.py -- parent class for our query trees
"""

class GameTree:
    def __init__(self, question, ynode=None, nnode=None):
        self.question = question
        self.yesNode = ynode
        self.noNode = nnode

    def play(self):
        return self