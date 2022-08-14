#  --- Directions
#  1) Implement the Node class to create
#  a binary search tree.  The constructor
#  should initialize values 'data', 'left',
#  and 'right'.
#  2) Implement the 'insert' method for the
#  Node class.  Insert should accept an argument
#  'data', then create an insert a new node
#  at the appropriate location in the tree.
#  3) Implement the 'contains' method for the Node
#  class.  Contains should accept a 'data' argument
#  and return the Node in the tree with the same value.
#  If the value isn't in the tree return null.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # def insert(self, data):
    #     new_node = Node(data)
    #     current_node = self

    #     while True:

    #         if current_node.data > data:

    #             if current_node.left != None:
    #               current_node = current_node.left
    #             else:
    #               current_node.left = new_node
    #               return

    #         if current_node.data < data:

    #             if current_node.right != None:
    #               current_node = current_node.right
    #             else:
    #               current_node.right = new_node
    #               return

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


    def insert(self, data):
      if (data < self.data and self.left):
          self.left.insert(data)
      elif (data < self.data):
          self.left = Node(data)
      elif (data > self.data and self.right):
          self.right.insert(data)
      elif (data > self.data):
          self.right = Node(data)
    
