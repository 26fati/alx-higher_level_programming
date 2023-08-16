#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lst in matrix:
        i = list(map(lambda x: x**2, lst))
        new_matrix.append(i)
    return new_matrix
