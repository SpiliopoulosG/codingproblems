from unittest.mock import patch
import io
import unittest
import types
from main import vowels


class TestVowels(unittest.TestCase):

    def test_vowels_exist(self):
        self.assertIsInstance(vowels, types.FunctionType)

    def test_vowels_aeiou(self):
        self.assertEqual((vowels("aeiou")), 5, "Should be 5")

    def test_vowels_30chars(self):
        self.assertEqual(
            (vowels("abcdefghijklmnopqrstuvwxyz")), 5, "Should be 5")

    def test_vowels_10chars(self):
        self.assertEqual(
            (vowels("bcdfghjkl")), 0, "Should be 0")

    def test_vowels_hello(self):
        self.assertEqual(
            (vowels("Hi There")), 3, "Should be 3")

    def test_vowels_question(self):
        self.assertEqual(
            (vowels("Why do you ask?")), 4, "Should be 4")

    def test_vowels_question(self):
        self.assertEqual(
            (vowels("Why?")), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()

