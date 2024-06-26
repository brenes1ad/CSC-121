"""
answers.py -- answers to assignment

Tony Brenes
CSC121 W24
3/30/24
"""

#R1
def secondToLast(head):
    current = head
    while current.next.next is not None:
        current = current.next
    return current

#R2
def concatList(L,M):
    current = L
    while current.next is not None:
        current = current.next
    current.next = M
    return L

#R3
def traverseCount(head,count=0):
    if head is None: return count
    count += 1
    return traverseCount(head.next, count)

#R4
"""find x_next, x_prev, y_next, y_prev makes swaps
x_prev, x_next = y_prev, y_next
"""

#R5
def countCircular(head):
    count = 0
    current = head.next
    while current != head:
        count += 1
        current = current.next
    return count

#R6
"""traverse forward through one and backward through other and look for like nodes"""


#R7
def rotate(self):
    if not self.is_empty():
        self.enqueue(self.dequeue())

#R8
"""iterate from front going in and back going in to find where they point to the same one or each other
 once they point to the same one, that's the middle and if they point to each other, you would return 
 the forward header.next since it's the one on the left.
 """

#R9
"""
L1End = list1.trailer.next
L2Begin = list2.header.next

L1.end.next = L2Begin
"""