#!/usr/bin/python3
""" Module for test Base class """
import unittest
import json
import os
import csv
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        # Create some instances of Base for testing
        Base._Base__nb_objects = 0

    def tearDown(self):
        # Clean up any files created during testing
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_id(self):
        """ Test default id """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_init(self):
        obj2 = Base(12)
        self.assertEqual(obj2.id, 12)

    def test_id_as_string(self):
        ''' test id as a string'''
        obj3 = Base('3')
        self.assertEqual(obj3.id, '3')

    def test_many_id(self):
        ''' test mix id '''
        obj1 = Base()
        obj2 = Base(122)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 122)
        self.assertEqual(obj3.id, 2)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            obj = Base(10, 10)

    def test_to_json_string(self):
        # Test with an empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test with None
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        # Test saving to a JSON file
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(data, res)

    def test_from_json_string(self):
        # Test loading from json string

        # Test with an empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test with None
        self.assertEqual(Base.from_json_string(None), [])

    def test_create(self):
        # Test creating an instance from a dictionary
        dic = {"id": 42}
        instance = Square.create(**dic)
        self.assertEqual(instance.id, 42)

    def test_save_to_file2(self):
        Square.save_to_file([])
        res = "[]"
        with open("Square.json", "r") as f:
            data = f.read()
            self.assertEqual(data, res)


if __name__ == "__main__":
    unittest.main()
