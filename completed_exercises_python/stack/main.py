#  --- Directions
#  Create a stack data structure.  The stack
#  should be a class with methods 'push', 'pop', and
#  'peek'.  Adding an element to the stack should
#  store it until it is removed.
#  --- Examples
#  const s = new Stack()
#  s.push(1)
#  s.push(2)
#  s.pop() // returns 2
#  s.pop() // returns 1

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

