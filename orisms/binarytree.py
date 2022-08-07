from asyncio import new_event_loop


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
class BinaryTree:

    def __init__(self):
        self.root = None
        
    def printTree(self):
        node = self.root
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.right
        print(nodes)
        return nodes

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.value > value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if self.root.value == value:
            return self.root
        else:
            current_node = self.root
            while True:
                if current_node.value == value:
                    return current_node
                if current_node.value > value:
                    if current_node.left is None:
                            return None
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                            return None
                    current_node = current_node.right
                    
    def remove(self, value):
        if self.root.value == value:
            self.root = None
            return self
        else:
            current_node = self.root
            node_to_replace = None
            while True:
                if current_node.value == value:
                    
                    node_to_replace = current_node
                    current_node = current_node.right
                    while True:
                        if current_node.left is None:
                            return current_node
                        current_node = current_node.left
                        
                if current_node.value > value:
                    if current_node.left is None:
                            return None
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                            return None
                    current_node = current_node.right

mybinarytree = BinaryTree()
mybinarytree.insert(9)
mybinarytree.insert(4)
mybinarytree.insert(6)
mybinarytree.insert(20)
mybinarytree.insert(170)
mybinarytree.insert(15)
mybinarytree.insert(1)
print(mybinarytree.lookup(11))
mybinarytree.printTree()
