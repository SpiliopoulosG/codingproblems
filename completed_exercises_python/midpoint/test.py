import types
import unittest

from linkedlist import LinkedList, Node
from main import midpoint


class TestMidPoint(unittest.TestCase):
    """Test Midpoint Function"""

    def test_midpoint_exist(self):
        """Test Midpoint exists"""
        self.assertIsInstance(midpoint, types.FunctionType)

    def test_midpoint_with_3_elements(self):
        """Test Midpoint with 3 elements"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        self.assertEqual(midpoint(linkedlist).data, "b")

    def test_midpoint_with_5_elements(self):
        """Test Midpoint with 5 elements"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.insert_last('d')
        linkedlist.insert_last('e')
        self.assertEqual(midpoint(linkedlist).data, "c")

    def test_midpoint_with_2_elements(self):
        """Test Midpoint with 2 elements"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        self.assertEqual(midpoint(linkedlist).data, "a")

    def test_midpoint_with_4_elements(self):
        """Test Midpoint with 4 elements"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.insert_last('d')
        self.assertEqual(midpoint(linkedlist).data, "b")
        