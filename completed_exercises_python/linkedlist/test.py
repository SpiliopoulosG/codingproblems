from os import link
import unittest
import types
from main import LinkedList, Node

class TestLinkedList(unittest.TestCase):


    
    def test_LinkedList_exist(self):
        self.assertIsInstance(LinkedList.__init__, types.FunctionType)

    def test_Node_exist(self):
        self.assertIsInstance(Node.__init__, types.FunctionType)

    def test_Node(self):
        node = Node('a', 'b')
        self.assertEqual(node.data, "a")
        self.assertEqual(node.next, "b")

    def test_insert_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.head.data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.head.data, 2)

    def test_size(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.size(), 0)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.size(), 4)

    def test_get_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_first().data, 1)
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_first().data, 2)

    def test_get_last(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(2)
        self.assertEqual(linkedlist.get_last().data, 2)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.get_last().data, 2)

    def test_clear(self):
        linkedlist = LinkedList()
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        linkedlist.insert_first(1)
        self.assertEqual(linkedlist.size(), 4)
        linkedlist.clear()
        self.assertEqual(linkedlist.size(), 0)

    def test_remove_first(self):
        linkedlist = LinkedList()
        linkedlist.insert_first('a')
        linkedlist.remove_first()
        self.assertEqual(linkedlist.size(), 0)
        self.assertEqual(linkedlist.get_first(), None)

    def test_remove_first_with_3_nodes(self):
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
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.remove_last(), None)

    def test_remove_last_with_1_node(self):
        linkedlist = LinkedList()
        linkedlist.insert_first('a')
        linkedlist.remove_last()
        self.assertEqual(linkedlist.size(), 0)
        self.assertEqual(linkedlist.head, None)

    def test_remove_last_with_2_node(self):
        linkedlist = LinkedList()
        linkedlist.insert_first('b')
        linkedlist.insert_first('a')
        linkedlist.remove_last()
        self.assertEqual(linkedlist.size(), 1)
        self.assertEqual(linkedlist.head.data, 'a')

    def test_remove_last_with_3_node(self):
            linkedlist = LinkedList()
            linkedlist.insert_first('c')
            linkedlist.insert_first('b')
            linkedlist.insert_first('a')
            linkedlist.remove_last()
            self.assertEqual(linkedlist.size(), 2)
            self.assertEqual(linkedlist.get_last().data, 'b')




if __name__ == '__main__':
    unittest.main()


# describe('InsertLast', () => {
#   test('adds to the end of the list', () => {
#     const l = new List();
#     l.insertFirst('a');

#     l.insertLast('b');

#     expect(l.size()).toEqual(2);
#     expect(l.getLast().data).toEqual('b');
#   });
# });

# describe('GetAt', () => {
#   test('returns the node at given index', () => {
#     const l = new List();
#     expect(l.getAt(10)).toEqual(null);

#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);

#     expect(l.getAt(0).data).toEqual(1);
#     expect(l.getAt(1).data).toEqual(2);
#     expect(l.getAt(2).data).toEqual(3);
#     expect(l.getAt(3).data).toEqual(4);
#   });
# });

# describe('RemoveAt', () => {
#   test('removeAt doesnt crash on an empty list', () => {
#     const l = new List();
#     expect(() => {
#       l.removeAt(0);
#       l.removeAt(1);
#       l.removeAt(2);
#     }).not.toThrow();
#   });

#   test('removeAt doesnt crash on an index out of bounds', () => {
#     const l = new List();
#     expect(() => {
#       const l = new List();
#       l.insertFirst('a');
#       l.removeAt(1);
#     }).not.toThrow();
#   });

#   test('removeAt deletes the first node', () => {
#     const l = new List();
#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);
#     expect(l.getAt(0).data).toEqual(1);
#     l.removeAt(0);
#     expect(l.getAt(0).data).toEqual(2);
#   });

#   test('removeAt deletes the node at the given index', () => {
#     const l = new List();
#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);
#     expect(l.getAt(1).data).toEqual(2);
#     l.removeAt(1);
#     expect(l.getAt(1).data).toEqual(3);
#   });

#   test('removeAt works on the last node', () => {
#     const l = new List();
#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);
#     expect(l.getAt(3).data).toEqual(4);
#     l.removeAt(3);
#     expect(l.getAt(3)).toEqual(null);
#   });
# });

# describe('InsertAt', () => {
#   test('inserts a new node with data at the 0 index when the list is empty', () => {
#     const l = new List();
#     l.insertAt('hi', 0);
#     expect(l.getFirst().data).toEqual('hi');
#   });

#   test('inserts a new node with data at the 0 index when the list has elements', () => {
#     const l = new List();
#     l.insertLast('a');
#     l.insertLast('b');
#     l.insertLast('c');
#     l.insertAt('hi', 0);
#     expect(l.getAt(0).data).toEqual('hi');
#     expect(l.getAt(1).data).toEqual('a');
#     expect(l.getAt(2).data).toEqual('b');
#     expect(l.getAt(3).data).toEqual('c');
#   });

#   test('inserts a new node with data at a middle index', () => {
#     const l = new List();
#     l.insertLast('a');
#     l.insertLast('b');
#     l.insertLast('c');
#     l.insertLast('d');
#     l.insertAt('hi', 2);
#     expect(l.getAt(0).data).toEqual('a');
#     expect(l.getAt(1).data).toEqual('b');
#     expect(l.getAt(2).data).toEqual('hi');
#     expect(l.getAt(3).data).toEqual('c');
#     expect(l.getAt(4).data).toEqual('d');
#   });

#   test('inserts a new node with data at a last index', () => {
#     const l = new List();
#     l.insertLast('a');
#     l.insertLast('b');
#     l.insertAt('hi', 2);
#     expect(l.getAt(0).data).toEqual('a');
#     expect(l.getAt(1).data).toEqual('b');
#     expect(l.getAt(2).data).toEqual('hi');
#   });

#   test('insert a new node when index is out of bounds', () => {
#     const l = new List();
#     l.insertLast('a');
#     l.insertLast('b');
#     l.insertAt('hi', 30);

#     expect(l.getAt(0).data).toEqual('a');
#     expect(l.getAt(1).data).toEqual('b');
#     expect(l.getAt(2).data).toEqual('hi');
#   });
# });

# describe('ForEach', () => {
#   test('applies a transform to each node', () => {
#     const l = new List();

#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);

#     l.forEach(node => {
#       node.data += 10;
#     });

#     expect(l.getAt(0).data).toEqual(11);
#     expect(l.getAt(1).data).toEqual(12);
#     expect(l.getAt(2).data).toEqual(13);
#     expect(l.getAt(3).data).toEqual(14);
#   });
# });

# describe('for...of loops', () => {
#   test('works with the linked list', () => {
#     const l = new List();

#     l.insertLast(1);
#     l.insertLast(2);
#     l.insertLast(3);
#     l.insertLast(4);

#     for (let node of l) {
#       node.data += 10;
#     }

#     expect(l.getAt(0).data).toEqual(11);
#     expect(l.getAt(1).data).toEqual(12);
#     expect(l.getAt(2).data).toEqual(13);
#     expect(l.getAt(3).data).toEqual(14);
#   });

#   test('for...of works on an empty list', () => {
#     const l = new List();
#     expect(() => {
#       for (let node of l) {
#       }
#     }).not.toThrow();
#   });
# });
