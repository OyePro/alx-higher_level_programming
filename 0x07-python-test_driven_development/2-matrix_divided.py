#!/usr/bin/python3
"""defining a function to divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Return new matrix with divisor
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if matrix is None or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the "
                            "same size")
        new_list = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            if isinstance(element, bool):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_list.append(round(element/div, 2))
        new_matrix.append(new_list)
    return (new_matrix)
