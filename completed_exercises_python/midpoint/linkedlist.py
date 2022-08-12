"""LinkedList and Node Module"""

class Node:
    """Makes a node to be appended in a linked list"""
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

class LinkedList:
    """A class for Linked Lists"""

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
        """Removes the last element from the linked list"""
        if self.size() == 1:
            self.head = None
        if self.size() != 0:
            node = self.head
            previous = self.head
            while node.next is not None:
                previous = node
                node = node.next
            previous.next = None
        else:
            return None

    def insert_first(self, value):
        """Insert value at the start of the list"""
        self.head = Node(value, self.head)

    def insert_last(self, value):
        """Insert value at the end of the list"""
        if self.head is None:
            self.insert_first(value)
            return
        new_node = Node(value)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def get_at(self, index):
        """Gets a node from the linked list at the given index"""
        if self.size() < index or self.size() == 0:
            return None
        node = self.head
        counter = 0
        while node is not None:
            if counter == index:
                return node
            node = node.next
            counter += 1

    def remove_at(self, index):
        """Removes a node from the list at the given index"""
        if self.size() < index or self.size() == 0:
            return None
        if index ==  0:
            return self.remove_first()
        previous_node = self.get_at(index - 1)
        node = self.get_at(index)
        previous_node.next = node.next

    def insert_at(self, index, value):
        """Insert a node from the list at the given index"""
        if self.size() < index or self.size() == 0:
            return self.insert_last(value)
        if index ==  0:
            return self.insert_first(value)
        previous_node = self.get_at(index - 1)
        node = self.get_at(index)
        new_node = Node(value, node)
        previous_node.next = new_node

    def __iter__(self):
        """Iters over the entire linked list"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        """Prints the entire linked list in a --> way"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
