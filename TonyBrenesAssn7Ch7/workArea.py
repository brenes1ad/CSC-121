"""
workArea.py --

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
one = Node(5)
two = Node(6)
three = Node(7)
one.next = two
two.next = three
three.next = one

