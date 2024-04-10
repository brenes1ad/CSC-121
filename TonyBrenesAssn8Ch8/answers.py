"""
answers.py -- worked out answers and testing to textbook answers
Tony Brenes
CSC121 W24
4/4/2024
"""
from arrayBinaryTree import ArrayBinaryTree
from linkedTree import LinkedTree

#R1
"""a.) /user/rt/courses/"""
"""b.) every node except the one mentioned above, grades, buylow, sellhigh, and market """
"""c.) 3"""
"""d.) 1"""
"""e.) grades and programs/"""
"""f.) papers/, demos/, buylow, sellhigh, market"""
"""g.) 1"""
"""h.) 5"""

#P64
tree = ArrayBinaryTree(10)
tree.setRoot(1)
tree.addLeftChild(1, 2)
tree.addRightChild(1, 3)
tree.addLeftChild(2, 4)
tree.addRightChild(2, 5)
tree.addRightChild(3,12)

for i in range(10):
    print(tree.tree[i])

tree = LinkedTree()
tree.addRoot("car")
tree.addChild(tree.getroot(), "wheel")
tree.addChild(tree.getroot(), "seats")
print(tree.getroot().node.childrenList)
