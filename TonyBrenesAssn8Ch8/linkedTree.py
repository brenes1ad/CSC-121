"""
linkedTree.py -- implementation of linked tre ADT from textbook

Tony Brenes
CSC121 W24
4/4/2024
"""
class LinkedTree():
    class Node:
        def __init__(self, element, parent=None, childrenList = []):
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
            return LinkedTree.Position(self, node) if node is not None else None