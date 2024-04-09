"""
workArea.py --

"""
class Position:
    def __init__(self, container, node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

    def __eq__(self, other):
        return type(other) is type(self) and other.node is self.node

    def validate(self, p):
        if not isinstance(p, Position):
            raise TypeError("p must be a proper Position type")
        if p.container is not self.container:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        return Position(None, node) if node is not None else None

