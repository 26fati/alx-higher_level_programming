#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
import json
import os
import csv
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import contextlib


class TestBase(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        # Create some instances of Base for testing
        Base._Base__nb_objects = 0

    def tearDown(self):
        # Clean up any files created during testing
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_init(self):
        ''' test Rectangle '''
        rec = Rectangle(20, 3)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)

    def test_rectangle(self):
        ''' test Rectangle '''
        rec = Rectangle(20, 3, 3, 3, 5)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 3)
        self.assertEqual(rec.id, 5)

    def test_rect_without_arg(self):
        ''' test without arguments'''
        with self.assertRaises(TypeError):
            rec = Rectangle()

    def test_rect_with_1arg(self):
        ''' test with one argument'''
        with self.assertRaises(TypeError):
            rec = Rectangle(3)

    def test_rect(self):
        ''' test validate arguments'''
        with self.assertRaises(TypeError):
            rec = Rectangle("4", 4, 5, 6, 5)

    def test_rect2(self):
        ''' test validate arguments'''
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 0, 5, 5, 5)

    def test_rect3(self):
        ''' test validate arguments'''
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 4, "5", 5, 6)

    def test_rec4(self):
        ''' test validate arguments'''
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 4, 5, -6)

    def test_access_private_attr(self):
        ''' test access private attribute'''
        rec = Rectangle(2, 4)
        with self.assertRaises(AttributeError):
            rec.__width

    def test_set_private_attr(self):
        ''' test set private attribute'''
        rec = Rectangle(4, 3, 4, 5, 3)
        rec.x = 5
        self.assertEqual(rec.x, 5)

    def test_area(self):
        ''' test area method'''
        rec = Rectangle(3, 4)
        self.assertEqual(rec.area(), 12)

    def test_display(self):
        ''' test display method'''
        rec = Rectangle(2, 2, 1, 1)
        res = "\n ##\n ##\n"
        str_out = StringIO()
        with contextlib.redirect_stdout(str_out):
            rec.display()
        self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        ''' test __str__ method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        string = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), string)

    def test_to_dictionary(self):
        ''' test to_dictionary method'''
        r1 = Rectangle(10, 2, 1, 9)
        res = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n"
        r1_dictionary = r1.to_dictionary()
        dic = StringIO()
        with contextlib.redirect_stdout(dic):
            print(r1_dictionary)
        dic = dic.getvalue()
        self.assertEqual(dic, res)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 5}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 5)

    def test_load_from_file_1(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()

        for i in range(len(list_input)):
            self.assertEqual(list_input[i].__str__(), list_output[i].__str__())


if __name__ == "__main__":
    unittest.main()
