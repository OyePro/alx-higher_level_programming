#!/usr/bin/python3
"""Defining function matrix_mul which multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """
    Return product of two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
            if isinstance(element, bool):
                raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        if not isinstance(rows, list):
            raise TypeError("m_b must be a list of lists")
        if len(rows) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for elements in rows:
            if not isinstance(elements, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
            if isinstance(elements, bool):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(i * j for i, j in zip(m_a_row, m_b_col))
              for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return (result)
