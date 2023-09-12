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
        lst = [1]
        if i > 0:
            prev_row = result[i - 1]
            for j in range(1, i):
                lst.append(prev_row[j - 1] + prev_row[j])
            lst.append(1)
        result.append(lst)
    return result
