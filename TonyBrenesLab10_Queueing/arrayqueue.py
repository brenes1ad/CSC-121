"""
arrayqueue.py -- create a queue using a resizable circular array, implement using Python lists

Tony Brenes
CSC121 W24
3/19/24
"""

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def enqueue(self, e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walker = self.front
        for k in range(self.size):
            self.data[k] = old[walker]
            walker = (walker + 1) % len(old)
        self.front = 0
