#  --- Directions
#  1) Create a node class.  The constructor
#  should accept an argument that gets assigned
#  to the data property and initialize an
#  empty array for storing children. The node
#  class should have methods 'add' and 'remove'.
#  2) Create a tree class. The tree constructor
#  should initialize a 'root' property to null.
#  3) Implement 'traverseBF' and 'traverseDF'
#  on the tree class.  Each method should accept a
#  function that gets called with each element in the tree


class Node:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))

    def remove(self, data):
        self.children = list(filter(lambda node: node.data != data, self.children))

class Tree:
    
    def __init__(self):
        self.root = None

    def traverse_bf(self, fn):
        arr = [self.root]
        while len(arr) > 0:
            node = arr.pop(0)
            for child in node.children:
                arr.append(child)
            fn(node)

    def traverse_df(self, fn):
        arr = [self.root]
        while len(arr) > 0:
            node = arr.pop(0)
            for child in node.children:
                arr.insert(0, child)
            fn(node)
