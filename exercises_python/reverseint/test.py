import unittest
import types
from main import reverseInt


class TestSum(unittest.TestCase):

    def test_reverse_exist(self):
        self.assertIsInstance(reverseInt, types.FunctionType)

    def test_reverseInt_positiveNumbers(self):
        self.assertEqual((reverseInt(0)), 0, "Should be 0")
        self.assertEqual((reverseInt(15)), 51, "Should be 51")
        self.assertEqual((reverseInt(90)), 9, "Should be 51")
        self.assertEqual((reverseInt(2359)), 9532, "Should be 51")

    def test_reverseInt_negativeNumbers(self):
        self.assertEqual((reverseInt(-5)), -5, "Should be 0")
        self.assertEqual((reverseInt(-15)), -51, "Should be 51")
        self.assertEqual((reverseInt(-90)), -9, "Should be 51")
        self.assertEqual((reverseInt(-2359)), -9532, "Should be 51")


if __name__ == '__main__':
    unittest.main()
