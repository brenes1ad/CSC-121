"""
text_array_priority_queue.py

Tony Brenes
CSC121 W24
3/19/24
"""
from arrayqueue import ArrayQueue

class TextArrPriorityQ(ArrayQueue):

    def enqueue(self, e):
        if not isinstance(e, str):
            raise TypeError("This PQueue only handles str values")
        super().enqueue(e)
        if self.size == 1:
            return
        dex = (self.front + self.size - 1) % len(self.data)
        prev = (dex - 1) % len(self.data)
        while dex != self.front and self.data[dex][0] < self.data[prev][0]:
            self.data[dex], self.data[prev] = self.data[prev], self.data[dex]
            dex = prev
            prev = (prev - 1) % len(self.data)

