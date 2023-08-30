#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """square class with it's size and proper validation"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position = position

    @position.setter
    def position(self, value):


    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size = 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)

