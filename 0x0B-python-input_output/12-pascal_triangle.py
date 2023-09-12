#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    result = []
    for i in range(n):
        input = [11 ** i]
        result.append(list(map(int, str(input[0]))))
    return result
