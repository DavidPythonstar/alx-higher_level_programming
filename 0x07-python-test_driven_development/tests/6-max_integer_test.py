#!/usr/bin/python3
"""Unit test for the max-int module"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for the max_int module"""

    def test_unordered(self):
        """Test for unordered list"""
        unorder = [7, 10, 8, 3, 14]
        self.assertEqual(max_integer(unorder), 14)

    def test_ordered(self):
        """Test for ordered list"""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_single(self):
        """Test for single value in a list"""
        single = [9]
        self.assertEqual(max_integer(single), 9)

    def test_neg(self):
        """Test for negative integers in list"""
        negatives = [-1, -10, -23]
        self.assertEqual(max_integer(negatives), -1)

    def test_empty(self):
        """Test for an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_mixed(self):
        """Test for mixed values list"""
        mixed = [7, -2, 10.3, 20]
        self.assertEqual(max_integer(mixed), 20)

if __name__ == '__main__':
unittest.main()
