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
        pass

    def getFirst(self):
        pass

    def getLast(self):
        pass

    def clear(self):
        pass

    def removeFirst(self):
        pass

    def removeLast(self):
        pass

    def insertLast(self, value):
        pass

    def getAt(self, index):
        pass

    def removeAt(self, index):
        pass

    def insertAt(self, index, value):
        pass

    def iter(self):
        pass
