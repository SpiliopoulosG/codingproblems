#  --- Description
#  Create a queue data structure.  The queue
#  should be a class with methods 'add' and 'remove'.
#  Adding to the queue should store an element until
#  it is removed
#  --- Examples
#  const q = new Queue();
#  q.enqueue(1);
#  q.dequeue(); // returns 1;

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
      return self.data[-1]

q = Queue()
q.enqueue(1)
q.enqueue(2)

