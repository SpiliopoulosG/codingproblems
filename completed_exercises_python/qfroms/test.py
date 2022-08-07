import unittest
import types
from main import Queue


class TestQueue(unittest.TestCase):

    def test_queue_exist(self):
        self.assertIsInstance(Queue.__init__, types.FunctionType)

    def test_queue_with_1_add(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual((q.dequeue()), 1, "Should be 1")

    def test_queue_with_3_add(self):
        q = Queue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        self.assertEqual((q.dequeue()), 1, "Should be 1")
        self.assertEqual((q.dequeue()), 2, "Should be 2")
        self.assertEqual((q.dequeue()), 3, "Should be 3")
        self.assertEqual((q.dequeue()), None, "Should be None")


if __name__ == '__main__':
    unittest.main()
