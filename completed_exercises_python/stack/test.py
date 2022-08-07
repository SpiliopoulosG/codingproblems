import unittest
import types
from main import Stack


class TestStack(unittest.TestCase):

    def test_Stack_exist(self):
        self.assertIsInstance(Stack.__init__, types.FunctionType)

    def test_stack_can_push_and_pop(self):
        s = Stack()
        s.push(1)
        self.assertEqual((s.pop()), 1, "Should be 1")
        s.push(2)
        self.assertEqual((s.pop()), 2, "Should be 2")

    def test_stack_with_3_push_and_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual((s.pop()), 3, "Should be 3")
        self.assertEqual((s.pop()), 2, "Should be 2")
        self.assertEqual((s.pop()), 1, "Should be 1")

    def test_stack_poek_works(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual((s.peek()), 3, "Should be 3")
        self.assertEqual((s.pop()), 3, "Should be 3")
        self.assertEqual((s.peek()), 2, "Should be 2")
        self.assertEqual((s.pop()), 2, "Should be 2")
        self.assertEqual((s.peek()), 1, "Should be 1")
        self.assertEqual((s.pop()), 1, "Should be 1")
        self.assertEqual((s.peek()), None, "Should be 'None'")



if __name__ == '__main__':
    unittest.main()

