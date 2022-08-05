import unittest
import types
from main import maxChar


class TestmaxChar(unittest.TestCase):

    def test_maxChar_exist(self):
        self.assertIsInstance(maxChar, types.FunctionType)

    def test_maxChar_characters(self):
        self.assertEqual((maxChar("a")), "a", "Should be a")
        self.assertEqual((maxChar("abcdefghijklmnaaaaa")), "a", "Should be a")
        self.assertEqual((maxChar("abcccccccd")), "c", "Should be c")

    def test_maxChar_numbers(self):
        self.assertEqual((maxChar("ab1c1d1e1f1g1")), "1", "Should be 1")
        self.assertEqual((maxChar("apple 1231111")), "1", "Should be 1")


if __name__ == '__main__':
    unittest.main()
    