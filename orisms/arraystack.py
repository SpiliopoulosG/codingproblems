class Stack:

    def __init__(self):
        self.nodes = []

    def printStack(self):
        return self.nodes

    def peek(self):
        if len(self.nodes) == 0:
            return self.nodes
        return self.nodes[len(self.nodes)-1]

    def push(self, value):
        self.nodes.append(value)
        return self

    def pop(self):
        if len(self.nodes) == 0:
            return "Can't delete an empty node."
        deletedData = self.nodes.pop(len(self.nodes)-1)
        return deletedData

myStack = Stack()
print(myStack.printStack())
myStack.push("Udemy")
myStack.push("Google")
myStack.push("Youtube")
print(myStack.printStack())
print(myStack.pop())
print(myStack.peek())