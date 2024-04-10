"""
linkedTree.py -- implementation of linked tre ADT from textbook

Tony Brenes
CSC121 W24
4/4/2024
"""
class LinkedTree():
    class Node:
        def __init__(self, element, parent=None, childrenList= []):
            self.element = element
            self.parent = parent
            # needs to be a list of references to children of node
            self.childrenList = childrenList

    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

    def validate(self, p):
        if not isinstance(p, LinkedTree.Position):
            raise TypeError("p must be a proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:
            raise ValueError("p is no longer valid")
        return p.node

    def makePosition(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def getroot(self):
        return self.makePosition(self.root)

    def parent(self, p):
        node = self.validate(p)
        return self.makePosition(node.parent)

    def addRoot(self, e):
        if self.root is not None: raise ValueError("Root Exists")
        self.size = 1
        self.root = self.Node(e)
        return self.makePosition(self.root)

    def addChild(self, p, e):
        node = self.validate(p)
        self.size += 1
        node.childrenList.append(self.Node(e, node))
        return self.makePosition(self.Node(e))
