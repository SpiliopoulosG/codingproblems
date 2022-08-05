import unittest
import types
from main import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzBuzz_exist(self):
        self.assertIsInstance(fizzBuzz, types.FunctionType)

    def test_number(self):
        self.assertEqual(fizzBuzz(1), 1)
        self.assertEqual(fizzBuzz(2), 2)
        self.assertEqual(fizzBuzz(4), 4)

    def test_multiple_3_should_return_fizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")

    def test_multiple_5_should_return_buzz(self):
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")

    def test_multiple_3_and_5_should_return_fizzbuzz(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
    


