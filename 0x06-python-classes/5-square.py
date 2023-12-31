#!/usr/bin/python3
"""Square class to represent a square"""


class Square:
    """square class with it's size and proper validation"""

    def __init__(self, size=0):
        self.__size = size

    """method to calculate the area of a square"""

    def area(self):
        return self.__size ** 2

    """get the private property"""

    @property
    def size(self):
        return self.__size
    """setter for size"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """print the square"""

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
