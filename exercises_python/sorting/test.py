import unittest
import types

from main import bubble_sort, merge, selection_sort, merge_sort


class TestSorting(unittest.TestCase):
    """Test Sorting Functions"""

    def test_bubble_sort(self):
        """Test bubble_sort can sort an array"""
        self.assertEqual(bubble_sort([101, -48, 400, -124, 0, 25, 9]), [-124, -48, 0, 9, 25, 101, 400])

    def test_selection_sort(self):
        """Test selection_sort function can sort an array"""                      
        self.assertEqual(selection_sort([101, -48, 400, -124, 0, 25, 9]), [-124, -48, 0, 9, 25, 101, 400])

    def test_Merge(self):
        """Test merge function can join together two sorted arrays"""
        left = [1, 9]
        right = [3, 5, 17]
        self.assertEqual(merge(left, right), [1, 3, 5, 9, 17])

    def test_Merge_sort(self):
        """Test merge_sort function  can sort an array"""
        self.assertEqual(merge_sort([101, -48, 400, -124, 0, 25, 9]), [-124, -48, 0, 9, 25, 101, 400])

