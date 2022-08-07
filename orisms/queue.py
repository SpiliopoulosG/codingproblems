class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def __iter__(self):
        node = self.last
        while node is not None:
            yield node
            node = node.next

    def printQueue(self):
        node = self.first
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        print(nodes)
        return nodes

    def peek(self):
        if self.length == 0:
            return None
        return self.first.data

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return self

    def dequeue(self):
        if self.first is None:
            return None

        if self.first is self.last:
            self.last = None

        deleted_data = self.first.data
        self.first = self.first.next
        self.length -= 1

        return deleted_data

my_queue = Queue()
my_queue.enqueue(Node("10"))
my_queue.enqueue(Node("150"))
my_queue.enqueue(Node("300"))
my_queue.enqueue(Node("20"))
print(my_queue.length)
my_queue.printQueue()
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
my_queue.printQueue()
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
my_queue.printQueue()
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
my_queue.printQueue()
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.length)
my_queue.printQueue()
print(my_queue.peek())