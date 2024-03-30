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
    if head is None: return
    count += 1
    traverseCount(head.next, count)

#R5
def countCircular(head):
    count = 0
    current = head.next
    while current != head:
        count += 1
        current = current.next
    return count