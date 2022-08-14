import unittest
import types

from main import validate
from node import Node


class TestValidate(unittest.TestCase):
    """Test validate Function"""

    def test_validate_exist(self):
        """Test Validate Function exists"""
        self.assertIsInstance(validate, types.FunctionType)

    def test_binary_validate_true(self):
        """Test validate recognizes a valid binary tree"""
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(0)
        node.insert(20)
        self.assertEqual(validate(node), True)

    def test_binary_validate_false(self):
        """Test validate recognizes an invalid binary tree"""
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(0)
        node.insert(20)
        node.left.left.right = Node(999)
        self.assertEqual(validate(node), False)
