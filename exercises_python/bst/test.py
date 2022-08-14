import unittest
import types

from main import Node


class TestTree(unittest.TestCase):
    """Test Tree Function"""

    def test_node_exist(self):
        """Test Node exists"""
        self.assertIsInstance(Node.__init__, types.FunctionType)

    def test_binary_tree(self):
        """Test Binary Tree"""
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(17)
        self.assertEqual(node.left.data, 5)
        self.assertEqual(node.right.data, 15)
        self.assertEqual(node.right.right.data, 17)

    def test_binary_tree_contains(self):
        """Test Binary Tree Contains function"""
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)
        three = node.left.left.right
        self.assertEqual(node.contains(3), three)

    def test_binary_tree_contains_when_not_exist(self):
        """Test Binary Tree Contains function"""
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)

        self.assertEqual(node.contains(9999), None)


