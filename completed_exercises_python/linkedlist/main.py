#  --- Directions
#  Implement classes Node and Linked Lists
#  See 'directions' document

class Node:

    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = None

    def size(self):
        """Return size of the linked list"""
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
            
        return count

    def get_first(self):
        """Return the first element of the linked list"""
        if self.size() != 0:
            return self.head
        return None

    def get_last(self):
        """Return the last element of the linked list"""
        if self.size() != 0:
            node = self.head
            while node is not None:
                if node.next is None:
                    return node
                node = node.next
        return None

    def clear(self):
        """Clears the entire linked list"""
        self.head = None

    def remove_first(self):
        """Removes the first element from the linked list"""
        if self.size() != 0:
            self.head = self.head.next
        else:
            return None

    def remove_last(self):
        if self.size() == 1:
            self.head = None
        if self.size() != 0:
            node = self.head
            previous = self.head
            while node is not None:
                if node.next is None:
                    previous.next = None
                previous = node
                node = node.next
        else:
            return None

    def insert_first(self, value):
        """Insert value at the start of the list"""
        self.head = Node(value, self.head)
        
    def insert_last(self, value):
        pass

    def getAt(self, index):
        pass

    def remove_at(self, index):
        pass

    def insert_at(self, index, value):
        pass

    def iter(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
l = LinkedList()
l.insert_first(10)
l.insert_first(20)
l.insert_first(80)
l.insert_first(40)
l.remove_last()
print(l.get_first().data)