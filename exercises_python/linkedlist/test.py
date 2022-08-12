import types
import unittest

from main import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    """Test LinkedList and Node Class"""

    def test_LinkedList_exist(self):
        """Test LinkedList constructor exists"""
        self.assertIsInstance(LinkedList.__init__, types.FunctionType)

    def test_Node_exist(self):
        """Test Node constructor exists"""
        self.assertIsInstance(Node.__init__, types.FunctionType)

    def test_Node(self):
        """Test Node data and next attributes work"""
        node = Node('a', 'b')
        self.assertEqual(node.data, "a")
        self.assertEqual(node.next, "b")

    def test_insert_first(self):
        """Test Insert on linked list on first index"""
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_size(self):
        """Test that the size of a linked list can be returned"""
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.size(), 0)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.size(), 4)

    def test_get_first(self):
        """Test that you can get the first element of the linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_first().data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_first().data, 2)

    def test_get_last(self):
        """Test that you can get the last element of the linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_last().data, 2)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_last().data, 2)

    def test_clear(self):
        """Test that the linked list can be cleared(emptied)"""
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.size(), 4)
        linkedlist.clear()
        self.assertEqual(linkedlist.size(), 0)

    def test_remove_first(self):
        """Test that the first element of a linkedlist is removed"""
        linkedlist = LinkedList()
        linkedlist.insert_first('a')
        linkedlist.remove_first()
        self.assertEqual(linkedlist.size(), 0)
        self.assertEqual(linkedlist.get_first(), None)

    def test_remove_first_with_3_nodes(self):
        """
        Test that the first element of a linked list is removed
        while other elements remain in the linked list
        """
        linkedlist = LinkedList()
        linkedlist.insert_first('c')
        linkedlist.insert_first('b')
        linkedlist.insert_first('a')
        linkedlist.remove_first()
        self.assertEqual(linkedlist.size(), 2)
        self.assertEqual(linkedlist.get_first().data, 'b')
        linkedlist.remove_first()
        self.assertEqual(linkedlist.size(), 1)
        self.assertEqual(linkedlist.get_first().data, 'c')

    def test_remove_last_empty(self):
        """Tests that remove_last don't break when called with empty linked list"""
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.remove_last(), None)

    def test_remove_last_with_1_node(self):
        """Test that the last element of a linkedlist is removed if it is the first"""
        linkedlist = LinkedList()
        linkedlist.insert_first('a')
        linkedlist.remove_last()
        self.assertEqual(linkedlist.size(), 0)
        self.assertEqual(linkedlist.head, None)

    def test_remove_last_with_2_node(self):
        """Test that the first element of a linkedlist is removed with 2 nodes"""
        linkedlist = LinkedList()
        linkedlist.insert_first('b')
        linkedlist.insert_first('a')
        linkedlist.remove_last()
        self.assertEqual(linkedlist.size(), 1)
        self.assertEqual(linkedlist.head.data, 'a')

    def test_remove_last_with_3_node(self):
        """Test that the first element of a linkedlist is removed with 3 nodes"""
        linkedlist = LinkedList()
        linkedlist.insert_first('c')
        linkedlist.insert_first('b')
        linkedlist.insert_first('a')
        linkedlist.remove_last()
        self.assertEqual(linkedlist.size(), 2)
        self.assertEqual(linkedlist.get_last().data, 'b')

    def test_insert_last(self):
        """Test that you can insert at the end of a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_first('a')
        linkedlist.insert_last('b')
        self.assertEqual(linkedlist.size(), 2)
        self.assertEqual(linkedlist.get_last().data, 'b')

    def test_get_at(self):
        """Test that you can get a node from a given index from a linked list"""
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.get_at(10), None)
        linkedlist.insert_last(1)
        linkedlist.insert_last(2)
        linkedlist.insert_last(3)
        linkedlist.insert_last(4)
        self.assertEqual(linkedlist.get_at(0).data, 1)
        self.assertEqual(linkedlist.get_at(1).data, 2)
        self.assertEqual(linkedlist.get_at(2).data, 3)
        self.assertEqual(linkedlist.get_at(3).data, 4)

    def test_remove_at(self):
        """Test that remove_at doesn't throw error at empty linked list"""
        linkedlist = LinkedList()
        linkedlist.remove_at(1)
        linkedlist.remove_at(2)
        linkedlist.remove_at(3)
        self.assertEqual(linkedlist.remove_at(0), None)
        self.assertEqual(linkedlist.remove_at(1), None)
        self.assertEqual(linkedlist.remove_at(2), None)

    def test_remove_at_out_of_index(self):
        """Test that remove_at doesn't break when index is out of range"""
        linkedlist = LinkedList()
        linkedlist.remove_at(10)
        self.assertEqual(linkedlist.remove_at(10), None)

    def test_remove_at_2(self):
        """Test that remove at works with a linked list with nodes"""
        linkedlist = LinkedList()
        linkedlist.insert_last(1)
        linkedlist.insert_last(2)
        linkedlist.insert_last(3)
        linkedlist.insert_last(4)
        self.assertEqual(linkedlist.get_at(0).data, 1)
        linkedlist.remove_at(0)
        self.assertEqual(linkedlist.get_at(0).data, 2)

    def test_remove_at_last_index(self):
        """Test remove at the last index of a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_last(1)
        linkedlist.insert_last(2)
        linkedlist.insert_last(3)
        linkedlist.insert_last(4)
        self.assertEqual(linkedlist.get_at(3).data, 4)
        linkedlist.remove_at(3)
        self.assertEqual(linkedlist.get_at(3), None)

    def test_insert_at_start(self):
        """Test insert on the start of the linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_at(0, 'hi')
        self.assertEqual(linkedlist.get_at(0).data, 'hi')

    def test_insert_at_start_with_others(self):
        """Test insert on the start of the linked list with other objects"""
        linkedlist = LinkedList()
        linkedlist.insert_last("a")
        linkedlist.insert_last("b")
        linkedlist.insert_last("c")
        linkedlist.insert_at(0, 'hi')
        self.assertEqual(linkedlist.get_at(0).data, 'hi')
        self.assertEqual(linkedlist.get_at(1).data, 'a')
        self.assertEqual(linkedlist.get_at(2).data, 'b')
        self.assertEqual(linkedlist.get_at(3).data, 'c')

    def test_insert_at(self):
        """Test insert can happen at a given index on a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_last("a")
        linkedlist.insert_last("b")
        linkedlist.insert_last("c")
        linkedlist.insert_last("d")
        linkedlist.insert_at(2, 'hi')
        self.assertEqual(linkedlist.get_at(0).data, 'a')
        self.assertEqual(linkedlist.get_at(1).data, 'b')
        self.assertEqual(linkedlist.get_at(2).data, 'hi')
        self.assertEqual(linkedlist.get_at(3).data, 'c')
        self.assertEqual(linkedlist.get_at(4).data, 'd')

    def test_insert_at_last_index(self):
        """Test insert at the last index of a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_last("a")
        linkedlist.insert_last("b")
        linkedlist.insert_at(2, 'hi')
        self.assertEqual(linkedlist.get_at(0).data, 'a')
        self.assertEqual(linkedlist.get_at(1).data, 'b')
        self.assertEqual(linkedlist.get_at(2).data, 'hi')

    def test_insert_at_out_of_index(self):
        """Test insert at out of index of a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_last("a")
        linkedlist.insert_last("b")
        linkedlist.insert_at(30, 'hi')
        self.assertEqual(linkedlist.get_at(0).data, 'a')
        self.assertEqual(linkedlist.get_at(1).data, 'b')
        self.assertEqual(linkedlist.get_at(2).data, 'hi')

    def test_iter_linkedlist(self):
        """Test that someone can iterate over a list of nodes in a linked list"""
        linkedlist = LinkedList()
        linkedlist.insert_last(1)
        linkedlist.insert_last(2)
        linkedlist.insert_last(3)
        linkedlist.insert_last(4)

        for node in linkedlist:
            node.data += 10

        self.assertEqual(linkedlist.get_at(0).data, 11)
        self.assertEqual(linkedlist.get_at(1).data, 12)
        self.assertEqual(linkedlist.get_at(2).data, 13)
        self.assertEqual(linkedlist.get_at(3).data, 14)

    def test_iter_empty_linkedlist(self):
        """Test that you can iter over an empty linkedlist without breaking the programm"""
        linkedlist = LinkedList()
        for node in linkedlist:
            print(node)

if __name__ == '__main__':
    unittest.main()
