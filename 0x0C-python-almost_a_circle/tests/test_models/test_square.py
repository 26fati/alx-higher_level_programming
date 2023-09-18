#!/usr/bin/python3
""" Module for test Square class """
import unittest
import json
import os
from models.square import Square
from models.base import Base
from io import StringIO
import contextlib


class TestBase(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        # Create some instances of Base for testing
        Base._Base__nb_objects = 0

    def tearDown(self):
        # Clean up any files created during testing
        for filename in ["Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_init(self):
        ''' test square'''
        s = Square(20)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square(self):
        ''' test square '''
        s = Square(20, 3, 3, 5)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 5)

    def test_square_without_arg(self):
        ''' test without arguments '''
        with self.assertRaises(TypeError):
            s = Square()

    def test_square(self):
        ''' test validate attributes '''
        with self.assertRaises(TypeError):
            s = Square("4", 4, 5, 6)

    def test_Square2(self):
        ''' test validate ayttributes'''
        with self.assertRaises(ValueError):
            s = Square(0, 0, 5, 5)

    def test_square3(self):
        ''' test validate attributes '''
        with self.assertRaises(TypeError):
            s = Square(4, 4, "5", 5)

    def test_square4(self):
        ''' test validate attributes'''
        with self.assertRaises(ValueError):
            s = Square(4, -4, 5, 8)

    def test_access_private_attr(self):
        ''' test access private attribute '''
        s = Square(2)
        with self.assertRaises(AttributeError):
            s.__size

    def test_set_private_attr(self):
        ''' test set private attribute '''
        s = Square(4, 3, 4, 5)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_area(self):
        ''' test area function '''
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        ''' test display function'''
        s = Square(2, 2, 1, 1)
        res = "\n  ##\n  ##\n"
        str_out = StringIO()
        with contextlib.redirect_stdout(str_out):
            s.display()
        self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        ''' test __str__ function'''
        s = Square(4, 6, 2, 1)
        string = "[Square] (1) 6/2 - 4"
        self.assertEqual(str(s), string)

    def test_to_dictionary(self):
        ''' test t0_dictionary function '''
        s = Square(10, 2, 1, 9)
        res = "{'id': 9, 'x': 2, 'size': 10, 'y': 1}\n"
        s1_dictionary = s.to_dictionary()
        dic = StringIO()
        with contextlib.redirect_stdout(dic):
            print(s1_dictionary)
        dic = dic.getvalue()
        self.assertEqual(dic, res)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 3, 'y': 5}
        s = Square.create(**dictionary)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_load_from_file_1(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5, 5)

        list_input = [s1, s2]
        Square.save_to_file(list_input)
        list_output = Square.load_from_file()

        for i in range(len(list_input)):
            self.assertEqual(list_input[i].__str__(), list_output[i].__str__())


if __name__ == "__main__":
    unittest.main()
