#!/usr/bin/python3
"""Defining functio pascal_triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    """
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(n - 1):
        row = [1]
        for j in range(i):
            row.append(tri[i][j] + tri[i][j + 1])
        row.append(1)
        tri.append(row)
    return (tri)
