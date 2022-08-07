import unittest
import types
from main import fib


class TestFib(unittest.TestCase):

    def test_fib_exist(self):
        self.assertIsInstance(fib, types.FunctionType)

    def test_fib_1(self):
        self.assertEqual((fib(1)), 1, "Should be 1")

    def test_fib_2(self):
        self.assertEqual((fib(2)), 1, "Should be 1")

    def test_fib_3(self):
        self.assertEqual((fib(3)), 2, "Should be 2")

    def test_fib_4(self):
        self.assertEqual((fib(4)), 3, "Should be 1")

    def test_fib_39(self):
        self.assertEqual((fib(39)), 63245986, "Should be 1")


if __name__ == '__main__':
    unittest.main()

