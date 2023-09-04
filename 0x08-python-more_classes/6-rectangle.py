#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    ''' a Rectangle class '''

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Arguments:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        ''' get the width of the rectangle.'''

        return self.__width

    @width.setter
    def width(self, value):
        ''' set the width of the rectangle.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' get the height of the rectangle.'''

        return self.__height

    @height.setter
    def height(self, value):
        ''' set the height of the rectangle.'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' return the rectangle area.'''
        return self.__height * self.__width

    def perimeter(self):
        ''' return the rectangle perimeter.'''
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = (self.__height + self.__width) * 2
        return perimeter

    def __str__(self):
        ''' return the representation of the rectangle with the # character.'''
        if self.__height == 0 or self.__width == 0:
            return ("")
        height = self.__height
        width = self.__width
        return '\n'.join("#" * width for i in range(height))

    def __repr__(self):
        ''' return a string representation of the rectangl'''
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
