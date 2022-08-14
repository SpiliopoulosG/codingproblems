import unittest
import types

from main import Tree, Node


class TestTree(unittest.TestCase):
    """Test Tree Function"""

    def test_Node_exist(self):
        """Test Node exists"""
        self.assertIsInstance(Node.__init__, types.FunctionType)

    def test_Tree_exist(self):
        """Test Tree exists"""
        self.assertIsInstance(Tree.__init__, types.FunctionType)

    def test_node_had_data_and_children(self):
        """Test Node has data and children"""
        node = Node('a')
        self.assertEqual(node.data, 'a')
        self.assertEqual(len(node.children), 0)

    def test_node_adds_children(self):
        """Test Node can add children"""
        node = Node('a')
        node.add('b')
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].children, [])

    def test_node_removes_children(self):
        """Test Node can remove children"""
        node = Node('a')
        node.add('b')
        self.assertEqual(len(node.children), 1)
        node.remove('b')
        self.assertEqual(len(node.children), 0)
    
    def test_tree_traverse_bf(self):
        """Test Tree traverse bf with a func"""
        characters = []
        tree = Tree()
        tree.root = Node('a')
        tree.root.add('b')
        tree.root.add('c')
        tree.root.children[0].add('d')
        tree.traverse_bf((lambda node: characters.append(node.data)))
        self.assertEqual(characters, ['a', 'b', 'c', 'd'])

    def test_tree_traverse_df(self):
        """Test Tree traverse df with a func"""
        characters = []
        tree = Tree()
        tree.root = Node('a')
        tree.root.add('b')
        tree.root.add('d')
        tree.root.children[0].add('c')
        tree.traverse_df((lambda node: characters.append(node.data)))
        self.assertEqual(characters, ['a', 'd', 'b', 'c'])
