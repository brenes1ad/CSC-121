"""
TreeSearchSort.py

Tony Brenes
CSC121 W24
4/5/2024
"""
from random import shuffle, choice

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inOrderPrint(self):
        # nlogn sorting
        # n traversal
        if self.left is not None:
            self.left.inOrderPrint()
        print(self.val)
        if self.right is not None:
            self.right.inOrderPrint()

    def find(self, wd):
        if wd == self.val:
            return True
        elif wd < self.val:
            if self.left is not None:
                return self.left.find(wd)
            else:
                return False
        elif wd > self.val:
            if self.right is not None:
                return self.right.find(wd)
            else:
                return False

with open("web2.txt", "r", encoding="utf-8") as f:
    text = f.readlines()

text = [wd[:-1] for wd in text]
shuffle(text)
# for i in text[:10]:
#     print(i)


def insert(t, val):
    """insert val into tree t in search-tree order"""
    if t is None:
        return TreeNode(val)
    else:
        if val < t.val:
            t.left = insert(t.left, val)
        else:
            t.right = insert(t.right, val)
        return t


tree = None
for i in range(10):
    val = choice(text)
    print(val)
    tree = insert(tree, val)

print("\n","inorder traversal of tree gives:", "\n")
tree.inOrderPrint()

print("\n","making a dictionary tree", "\n")
tree = None
for wd in text:
    tree = insert(tree, wd)
print("well, that's done")

print("console in tree? ", tree.find("console"))
print("spongebob in tree?", tree.find("spongebob"))
tree = insert(tree, "spongebob")
print("spongebob in tree?", tree.find("spongebob"))
