#  --- Directions
#  Implement a 'peek' method in this Queue class.
#  Peek should return the last element (the next
#  one to be returned) from the queue *without*
#  removing it.

class Queue:
  
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

