"""
arrayBinaryTree.py -- implementation of the binary tree ADT from the textbook

Tony Brenes
CSC121 W24
4/4/2024
"""

class ArrayBinaryTree:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * size
        self.rootPosition = None
        self.currentSize = 0

    def isEmpty(self):
        return self.currentSize == 0

    def setRoot(self, val):
        self.tree[1] = val
        self.rootPosition = 0
        self.currentSize += 1

    def addLeftChild(self, position, val):
        index = position * 2
        self.tree[index] = val
        self.currentSize += 1

    def addRightChild(self, position, val):
        index = position * 2 + 1
        self.tree[index] = val
        self.currentSize += 1





