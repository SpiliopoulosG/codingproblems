import unittest
import types

from main import level_width
from node import Node


class TestTree(unittest.TestCase):
    """Test Tree Function"""

    def test_level_widtj_exist(self):
        """Test level_width exists"""
        self.assertIsInstance(level_width, types.FunctionType)

    def test_level_width_1(self):
        """Test level_width with 3 elements widest level"""
        node = Node(0)
        node.add(1)
        node.add(2)
        node.add(3)
        node.children[0].add(4)
        node.children[2].add(5)
        self.assertEqual(level_width(node), [1, 3, 2])

    def test_level_width_2(self):
        """Test level_width with 4 elements widest level"""
        node = Node(0)
        node.add(1)
        node.children[0].add(4)
        node.children[0].add(3)
        node.children[0].children[0].add(4)
        self.assertEqual(level_width(node), [1, 1, 2, 1])
