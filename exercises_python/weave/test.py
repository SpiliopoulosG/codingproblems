import unittest
import types
from main import weave
from queue import Queue


class TestWeave(unittest.TestCase):

    def test_queue_peek_exist(self):
        self.assertIsInstance(Queue.peek, types.FunctionType)

    def test_queue_with_2_add(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual((q.dequeue()), 1, "Should be 1")
        self.assertEqual((q.dequeue()), 2, "Should be 2")

    def test_queue_with_4_add(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual((q.dequeue()), 1, "Should be 1")
        self.assertEqual((q.dequeue()), 2, "Should be 2")
        self.assertEqual((q.dequeue()), 3, "Should be 3")
        self.assertEqual((q.dequeue()), 4, "Should be 4")

    def test_weave_exist(self):
        self.assertIsInstance(weave, types.FunctionType)

    def test_weave_works(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)
        queue2 = Queue()
        queue2.enqueue("one")
        queue2.enqueue("two")
        queue2.enqueue("three")
        queue2.enqueue("four")

        weaved_gueue = weave(queue1, queue2)

        self.assertEqual((weaved_gueue.dequeue()), 1, "Should be 1")
        self.assertEqual((weaved_gueue.dequeue()), "one", "Should be 'one'")
        self.assertEqual((weaved_gueue.dequeue()), 2, "Should be 2")
        self.assertEqual((weaved_gueue.dequeue()), "two", "Should be 'two'")
        self.assertEqual((weaved_gueue.dequeue()), 3, "Should be 3")
        self.assertEqual((weaved_gueue.dequeue()), "three", "Should be 'three'")
        self.assertEqual((weaved_gueue.dequeue()), 4, "Should be 4")
        self.assertEqual((weaved_gueue.dequeue()), "four", "Should be 'four'")
    


if __name__ == '__main__':
    unittest.main()
