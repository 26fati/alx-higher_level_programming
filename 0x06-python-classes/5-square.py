#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square,
many things depend of it (area computation, etc.),
so you, as class builder, must control the type and value of this attribute.
One way to have the control is to keep it privately.

You will see in next tasks how to get,update and validate the size value.
"""


class Square():
    """square class with it's size and proper validation"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

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
