#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        result = []
        for i in matrix:
            result.append(i**2)
        return (result)
