#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max is the first element"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test a list where the max is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 0, -5]), 2)

    def test_one_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_floats_and_ints(self):
        """Test a list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.1]), 3)


if __name__ == '__main__':
    unittest.main()