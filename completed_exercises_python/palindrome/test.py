
import unittest
import types
from main import palindrome

class TestSum(unittest.TestCase):

    def test_reverse_exist(self):
        self.assertIsInstance(palindrome, types.FunctionType)

    def test_reverse_aba(self):
        self.assertTrue(palindrome("aba"))

    def test_reverse_aba1(self):
        self.assertFalse(palindrome(" aba"))

    def test_reverse_aba2(self):
        self.assertFalse(palindrome("aba "))

    def test_reverse_greetings(self):
        self.assertFalse(palindrome("greetings"))

    def test_reverse_1000000001(self):
        self.assertTrue(palindrome("1000000001"))

    def test_reverse_Fish1hsif(self):
        self.assertFalse(palindrome("'Fish hsif'"))

    def test_reverse_pennep(self):
        self.assertTrue(palindrome("pennep"))

    def test_reverse_abcdefg(self):
        self.assertFalse(palindrome("abcdefg"))


if __name__ == '__main__':
    unittest.main()
