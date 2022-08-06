import unittest
import types
from main import anagrams


class TestAnagrams(unittest.TestCase):

    def test_anagrams_exist(self):
        self.assertIsInstance(anagrams, types.FunctionType)

    def test_anagrams_hello(self):
        self.assertTrue(anagrams('hello', 'llohe'))

    def test_anagrams_whoahi(self):
        self.assertTrue(anagrams('Whoa! Hi!', 'Hi! Whoa!'))

    def test_anagrams_oneone1(self):
        self.assertFalse(anagrams('One One', 'Two two two'))

    def test_anagrams_oneone(self):
        self.assertFalse(anagrams('One one', 'One one c'))

    def test_anagrams_phrase(self):
        self.assertFalse(anagrams("A tree, a life, a bench",
                         "A tree, a fence, a yard"))




if __name__ == '__main__':
    unittest.main()
