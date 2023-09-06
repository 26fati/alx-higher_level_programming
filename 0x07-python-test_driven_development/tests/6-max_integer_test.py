#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_first_list(self):
        ''' test an ordered list of integers'''
        ordered_list = [7, 9, 11, 20]
        self.assertEqual(max_integer(ordered_list), 20)

    def test_unordered_list(self):
        ''' test unordered list of integers'''
        lst = [43, 87, 9, 0]
        self.assertEqual(max_integer(lst), 87)

    def test_at_begginning(self):
        ''' test list with maximum value at the begginning'''
        lst = [70, 8, 9, 40]
        self.assertEqual(max_integer(lst), 70)

    def test_integers_floats_list(self):
        ''' test a list with integers and floats'''
        lst = [5, 5.5, 8.5, 4, 2.5]
        self.assertEqual(max_integer(lst), 8.5)

    def test_empty_list(self):
        ''' test an empty list'''
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_one_element_list(self):
        ''' test a list with one element'''
        lst = [2]
        self.assertEqual(max_integer(lst), 2)

    def test_list_of_strings(self):
        ''' test a list of strings'''
        lst = ['hello', 'hi', 'Good']
        self.assertEqual(max_integer(lst), 'hi')

    def test_with_string(self):
        ''' test a string'''
        string = 'fatima'
        self.assertEqual(max_integer(string), 't')

    def test_with_empty_string(self):
        ''' test an empty string'''
        string = ''
        self.assertEqual(max_integer(string), None)

    def test_func_without_argument(self):
        ''' test function without arguments'''
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
