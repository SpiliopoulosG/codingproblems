import types
import unittest

from linkedlist import LinkedList, Node
from main import circular


class TestCircular(unittest.TestCase):
    """Test Circular Function"""

    def test_circular_exist(self):
        """Test Circular exists"""
        self.assertIsInstance(circular, types.FunctionType)

    def test_circular_pointing_at_midpoint(self):
        """Test Circular with 3 elements that points at midpoint"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.get_at(2).next = linkedlist.get_at(1)
        self.assertEqual(circular(linkedlist), True)

    def test_circular_pointing_at_start(self):
        """Test Circular with 3 elements that points at the start"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.get_at(2).next = linkedlist.get_at(0)
        self.assertEqual(circular(linkedlist), True)

    def test_false_circular_pointing_at_none(self):
        """Test Circular with 3 elements that points at the start"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.get_at(2).next = None
        self.assertEqual(circular(linkedlist), False)
