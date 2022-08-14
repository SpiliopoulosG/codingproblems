import unittest
import types

from linkedlist import LinkedList, Node
from main import fromlast


class TestFromLast(unittest.TestCase):
    """Test FromLast Function"""

    def test_FromLast_exist(self):
        """Test FromLast exists"""
        self.assertIsInstance(fromlast, types.FunctionType)

    def test_FromLast_pointing_at_midpoint(self):
        """Test FromLast with 3 elements that points at midpoint"""
        linkedlist = LinkedList()
        linkedlist.insert_last('a')
        linkedlist.insert_last('b')
        linkedlist.insert_last('c')
        linkedlist.insert_last('d')
        linkedlist.insert_last('e')
        self.assertEqual(fromlast(linkedlist,3).data, 'b')

