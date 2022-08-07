#  --- Directions
#  Implement a Queue datastructure using two stacks.
#  *Do not* create an array inside of the 'Queue' class.
#  Queue should implement the methods 'add', 'remove', and 'peek'.
#  For a reminder on what each method does, look back
#  at the Queue exercise.
#  --- Examples
#  const q = new Queue();
#  q.add(1);
#  q.add(2);
#  q.peek();  // returns 1
#  q.remove(); // returns 1
#  q.remove(); // returns 2

from stack import Stack

class Queue:

    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def enqueue(self, value):
        self.first.push(value)

    def dequeue(self):
        while self.first.peek() is not None:
            self.second.push(self.first.pop())

        record = self.second.pop()

        while self.second.peek() is not None:
            self.first.push(self.second.pop())

        return record

    def peek(self):
        while self.first.peek() is not None:
            self.second.push(self.first.pop())

        record = self.second[-1]

        while self.second.peek() is not None:
            self.first.push(self.second.pop())

        return record
