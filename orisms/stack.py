class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def printStack(self):
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return nodes

    def len(self):
        return self.length

    def peek(self):
        return self.top.data

    def push(self, value):
        node = Node(value)
        if self.bottom is None:
            self.bottom = node
            self.top = self.bottom
            self.length += 1
            return
        node.next = self.top
        self.top = node
        self.length += 1
        return self

    def pop(self):
        if self.top is None:
            return

        if self.top.next is None:
            self.bottom = None

        deletedData = self.top.data
        self.top = self.top.next
        self.length -= 1
        return deletedData

myStack = Stack()
print(myStack.printStack())
myStack.push(Node("10"))
myStack.push(Node("150"))
myStack.push(Node("300"))
myStack.push(Node("20"))
print(myStack.printStack())
print(myStack.len())
print(myStack.pop())
print(myStack.printStack())
print(myStack.len())
print(myStack.peek())