#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        result = []
        for i in matrix:
            result.append(list(map(lambda x: x**2, i)))
        return (result)
    return None
