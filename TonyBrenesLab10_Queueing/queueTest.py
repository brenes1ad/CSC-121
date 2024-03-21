"""
queueTest.py --

Tony Brenes
CSC121 W24
3/19/24
"""

# imports
from arrayqueue import ArrayQueue
from random import shuffle, choice
from text_array_priority_queue import TextArrPriorityQ as TextPQ


# read text from file, store as individual words in a list

with open("web2.txt", "r", encoding="utf8") as f:
    words = f.read()
    wordList = words.split()



# Create and test our ArrayQueue
arrQ = ArrayQueue()
# for i in range(10):
#     print("enqueueing %d" % i)
#     arrQ.enqueue(i)
#
# print("arrQ has %d elements" %len(arrQ))
#
# try:
#     while True:
#         print("removing %d" % arrQ.dequeue())
# except:
#     print("queue now empty")
# print("size of queue = %d" %len(arrQ))

print("")

# wordQ = ArrayQueue()
# for _ in range(10):
#     word = choice(wordList)
#     print(f"enqueueing {word}")
#     wordQ.enqueue(word)
# print("")
#
# try:
#     while True:
#         print(f"removing {wordQ.dequeue()}" )
# except:
#     print("queue now empty")
# print("size of queue = %d" %len(arrQ))


print("\n","TextArrayPriorityQueue")
# Create and test our TextArrayPriorityQueue

pq = TextPQ()
# pq.enqueue(wordList[20000])
# pq.enqueue(wordList[19000])
# pq.enqueue(wordList[5])
#
# print(f"len pq = {len(pq)}")
# print(f"popping! {pq.dequeue()}")
# print(f"popping! {pq.dequeue()}")
# print(f"popping! {pq.dequeue()}")

for _ in range(30):
    word = choice(wordList)
    print(f"enqueueing {word}")
    pq.enqueue(word)
print("")

try:
    while True:
        print(f"removing {pq.dequeue()}")
except:
    print("queue now empty")