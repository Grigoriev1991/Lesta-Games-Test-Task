import unittest
from random import randint

from quick_sort.quick_sort import bubble_sort, quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_array(self):
        arr = [5]
        self.assertEqual(quick_sort(arr), [5])
        self.assertEqual(bubble_sort(arr), [5])

    def test_array_with_duplicates(self):
        arr = [3, 2, 1, 3, 2, 1]
        arr_copy = arr.copy()
        self.assertEqual(quick_sort(arr_copy), [1, 1, 2, 2, 3, 3])
        arr_copy = arr.copy()
        self.assertEqual(bubble_sort(arr), [1, 1, 2, 2, 3, 3])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        arr_copy = arr.copy()
        self.assertEqual(quick_sort(arr_copy), [1, 2, 3, 4, 5])
        arr_copy = arr.copy()
        self.assertEqual(bubble_sort(arr_copy), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        arr_copy = arr.copy()
        self.assertEqual(quick_sort(arr_copy), [1, 2, 3, 4, 5])
        arr_copy = arr.copy()
        self.assertEqual(bubble_sort(arr_copy), [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [randint(0, 100) for _ in range(20)]
        sorted_array = sorted(arr)
        arr_copy = arr.copy()
        self.assertEqual(quick_sort(arr_copy), sorted_array)
        arr_copy = arr.copy()
        self.assertEqual(bubble_sort(arr_copy), sorted_array)


if __name__ == '__main__':
    unittest.main()
