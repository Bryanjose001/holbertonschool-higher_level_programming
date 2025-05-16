#!/usr/bin/python3
"""Divide all elements of a matrix by a given number and round to 2 decimal
    places."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number and round to 2 decimal
    places.
    """
    error = "matrix must be a matrix (array of arrays of integers/floats)"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(error)
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for index in rows:
            if type(index) not in (int, float):
                raise TypeError(error)
    return ([list(map(lambda x: round(x / div, 2), rows)) for rows in matrix])
