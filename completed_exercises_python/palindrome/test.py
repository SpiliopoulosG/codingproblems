
import unittest
import types
from main import palindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome_exist(self):
        self.assertIsInstance(palindrome, types.FunctionType)

    def test_palindrome_aba(self):
        self.assertTrue(palindrome("aba"))

    def test_palindrome_aba1(self):
        self.assertFalse(palindrome(" aba"))

    def test_palindrome_aba2(self):
        self.assertFalse(palindrome("aba "))

    def test_palindrome_greetings(self):
        self.assertFalse(palindrome("greetings"))

    def test_palindrome_1000000001(self):
        self.assertTrue(palindrome("1000000001"))

    def test_palindrome_Fish1hsif(self):
        self.assertFalse(palindrome("'Fish hsif'"))

    def test_palindrome_pennep(self):
        self.assertTrue(palindrome("pennep"))

    def test_palindrome_abcdefg(self):
        self.assertFalse(palindrome("abcdefg"))


if __name__ == '__main__':
    unittest.main()
