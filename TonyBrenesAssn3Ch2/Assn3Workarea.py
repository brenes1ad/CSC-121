
class Deque:
    """
    init, first, is_empty, len, add_first, remove_first, and resize all the same as queue
    """
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.front = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def resize(self, capacity):
        old = self.data
        self._data = [None] * capacity
        for i in range(len(old)):
            self._data[i] = old[(self.front + i) % len(old)]
        self._front = 0

    def len(self):
        return self.size

    def last(self):
        if self.isEmpty(): raise Exception("Empty Queue")
        return self.data[(self.front + self.size - 1) % len(self.data)]

    def addLast(self, e):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        self.data[(self.front + self.size) % len(self.data)] = e
        self.size += 1

    def removeLast(self):
        if self.isEmpty(): raise Exception("Empty Queue")
        answer = self.data[(self.front + self.size - 1) % len(self.data)]
        self.data[(self.front + self.size - 1) % len(self.data)] = None
        self.size -= 1
        return answer







