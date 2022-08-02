
from cgi import print_environ_usage
from hashlib import new
from os import pread


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
    def prepend(self, node):
        node.next = self.head
        self.head = node

    def insert(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def reverse(self):
        if not self.head.next:
            return self.head
        
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            print(f"\nSecond is:{second}")
            temp = second.next
            print(f"\nTemp is now:{temp} or {second}.next")
            second.next = first
            print(f"\nSecond.next is now:{first} or first")
            first = second
            print(f"\nFirst is now:{second}" )
            second = temp
            print(f"\nSecond is now:{temp}" )
        self.head.next = None
        self.head = first
        return self
            

mylinkedlist = LinkedList(["a", "b", "c", "d", "e"])
# mylinkedlist.prepend(Node("10"))
# mylinkedlist.append(Node("20"))
# mylinkedlist.insert("b", Node("16"))
# mylinkedlist.remove("c")
print(mylinkedlist)
print(mylinkedlist.reverse())

# mylinkedlist.append(5)
# mylinkedlist.append(16)
# mylinkedlist.prepend(1)
# print(mylinkedlist.printList())
