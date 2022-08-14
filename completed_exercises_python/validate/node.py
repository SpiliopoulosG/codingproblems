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
        self.left = None
        self.right = None

    def insert(self, data):
        new_node = Node(data)
        current_node = self

        while True:

            if current_node.data > data:

                if current_node.left != None:
                  current_node = current_node.left
                else:
                  current_node.left = new_node
                  return

            if current_node.data < data:

                if current_node.right != None:
                  current_node = current_node.right
                else:
                  current_node.right = new_node
                  return

    def contains(self, data):

        current_node = self

        while True:

            if current_node.data == data:
              return current_node

            if current_node.data > data:

                if current_node.left != None:
                  current_node = current_node.left
                else:
                  return None

            if current_node.data < data:

                if current_node.left != None:
                  current_node = current_node.right
                else:
                  return None
