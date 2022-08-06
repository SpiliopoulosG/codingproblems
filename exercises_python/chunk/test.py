import unittest
import types
from main import chunk


class TestmaxChar(unittest.TestCase):

    def test_chunk_exist(self):
        self.assertIsInstance(chunk, types.FunctionType)

    def test_chunk_10with2(self):
      arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      self.assertEqual((chunk(arr, 2)), [[1, 2], [3, 4], [
                       5, 6], [7, 8], [9, 10]])

    def test_chunk_3with1(self):
      arr = [1, 2, 3]
      self.assertEqual((chunk(arr, 1)), [[1], [2], [3]])

    def test_chunk_5with3(self):
      arr = [1, 2, 3, 4, 5]
      self.assertEqual((chunk(arr, 3)), [[1, 2, 3], [4, 5]])

    def test_chunk_13with5(self):
      arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
      self.assertEqual((chunk(arr, 5)), [[1, 2, 3, 4, 5], [
                       6, 7, 8, 9, 10], [11, 12, 13]])


if __name__ == '__main__':
    unittest.main()