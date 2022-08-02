class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Queue:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def __iter__(self):
        node = self.bottom
        while node is not None:
            yield node
            node = node.next

    def printStack(self):
        node = self.bottom
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes

    def peek(self):
        return self.bottom.data

    def enqueue(self, value):
        node = Node(value)
        if self.bottom is None:
            self.bottom = node
            self.length += 1
            return
        for current_node in self:
            pass
        current_node.next = node
        self.length += 1

    def dequeue(self):
        if self.bottom is None:
            return "List is empty"

        if self.bottom.next is None:
            self.bottom = None

        deleted_data = self.bottom.data
        self.bottom = self.bottom.next
        self.length -= 1

        return deleted_data

my_queue = Queue()
my_queue.enqueue(Node("10"))
my_queue.enqueue(Node("150"))
my_queue.enqueue(Node("300"))
my_queue.enqueue(Node("20"))
print(my_queue.length)
print(my_queue.printStack())
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
print(my_queue.printStack())
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
print(my_queue.printStack())
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
print(my_queue.printStack())
print(my_queue.peek())
print(my_queue.dequeue())
