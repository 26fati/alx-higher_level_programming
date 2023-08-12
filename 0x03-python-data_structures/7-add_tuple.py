#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 < 2:
        tuple_a = tuple_a + (0, 0, )
    if len2 < 2:
        tuple_b = tuple_b + (0, 0, )
    element1 = tuple_a[0] + tuple_b[0]
    element2 = tuple_a[1] + tuple_b[1]
    new_tuple = (element1, element2)
    return new_tuple
