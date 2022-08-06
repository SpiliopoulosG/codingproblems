import unittest
import types
from main import capitalize


class TestCapitalize(unittest.TestCase):

    def test_capitalize_exist(self):
        self.assertIsInstance(capitalize, types.FunctionType)

    def test_capitalize_example1(self):
        self.assertEqual(capitalize('hi there, how is it going?'),
                        'Hi There, How Is It Going?')

    def test_capitalize_example2(self):
        self.assertEqual(capitalize(
            'a short sentence'), 'A Short Sentence')

    def test_capitalize_example3(self):
        self.assertEqual(capitalize(
            'a lazy fox'), 'A Lazy Fox')
  
    def test_capitalize_example4(self):
        self.assertEqual(capitalize(
            'look, it is working!'), 'Look, It Is Working!')


if __name__ == '__main__':
    unittest.main()
