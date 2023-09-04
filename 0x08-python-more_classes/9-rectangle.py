#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    ''' a Rectangle class

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    '''

    number_of_instances = 0
    print_symbol = "#"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area.

        Args:
           rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        ''' return the representation of the rectangle with the # character.'''
        if self.__height == 0 or self.__width == 0:
            return ("")
        height = self.__height
        width = self.__width
        return '\n'.join(str(self.print_symbol) * width for i in range(height))

    def __repr__(self):
        ''' return a string representation of the rectangl'''
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
