#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    ''' a Rectangle class '''

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Arguments:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' get the width of the rectangle'''

        return self.__width

    @width.setterdef
    def width(self, value):
        ''' set the width of the rectangle'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' get the height of the rectangle'''

        return self.__height

    @height.setter
    def height(self, value):
        ''' set the height of the rectangle'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' return the rectangle area'''
        return self.__height * self.__width

    def perimeter(self):
        ''' return the rectangle perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = (self.__height + self.__width) * 2
        return perimeter
