#!/usr/bin/python3
"""
 This is the 2-matrix_divided module.

 This module supplies one function, matrix_divided(). for example,

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix.

    Args:
        matrix (list[list]): The matrix to be divided
        div (int, float): The divisor

    Returns:
         A matrix with all elements divided by div

    Raises:
         TypeError: If matrix is not a list of lists of integers or floats
         TypeError: If all rows of the matrix don't have the same size
         TypeError: If div is not a number (integer or float)
         ZeroDivisionError: if div is equal to zero
    """
    if not matrix:
        return None
    if not all(isinstance(value, (int, float)) for row in matrix for value in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row]for row in matrix]
