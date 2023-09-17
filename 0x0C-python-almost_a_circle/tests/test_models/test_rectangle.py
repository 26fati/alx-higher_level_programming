#!/usr/bin/python3

import unittest
import json
import os
import csv
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        # Create some instances of Base for testing
        Base._Base__nb_objects = 0

    def tearDown(self):
        # Clean up any files created during testing
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_init(self):
        rec = Rectangle(20, 3)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)

    def test_rectangle(self):
        rec = Rectangle(20, 3, 3, 3, 5)
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 3)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 3)
        self.assertEqual(rec.id, 5)

    def test_rect_without_arg(self):
        with self.assertRaises(TypeError):
            rec = Rectangle()

    def test_rect_with_1arg(self):
        with self.assertRaises(TypeError):
            rec =  Rectangle(3)

    def test_rect(self):
        with self.assertRaises(TypeError):
            rec = Rectangle("4", 4, 5, 6, 5)

    def test_rect2(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 0, 5, 5, 5)

    def test_rect3(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 4, "5", 5, 6)

    def test_rec4(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(4, 4, 5, -6)

    def test_access_private_attr(self):
        rec = Rectangle(2, 4)
        # with self.assertRaises(AttributeError):
        rec.width

    def test_set_private_attr(self):
        rec = Rectangle(4, 3, 4, 5, 3)
        rec.x = 5
