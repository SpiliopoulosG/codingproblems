
import unittest
import types
from main import reverse

class TestReverseString(unittest.TestCase):

    def test_reverse_exist(self):
        self.assertIsInstance(reverse, types.FunctionType)

    def test_reverse_apple(self):
        self.assertEqual((reverse("apple")), "elppa", "Should be elppa")


    def test_reverse_hello(self):
        self.assertEqual((reverse("hello")), "olleh", "Should be olleh")

    def test_reverse_greetings(self):
        self.assertEqual((reverse("Greetings!")), "!sgniteerG", "Should be !sgniteerG")

    def test_reverse_abcd(self):
        self.assertEqual((reverse("abcd")), "dcba", "Should be dcba")

    def test_reverse_abcd(self):
        self.assertEqual((reverse("  abcd")), "dcba  ", "Should be dcba")



if __name__ == '__main__':
    unittest.main()
