#!/usr/bin/python3
"""Defining fuction lazy_matrix_mul which multiplies matrices easily"""

import numpy as mul


def lazy_matrix_mul(m_a, m_b):
    """
    Return product of two matrices
    """
    result = mul.matmul(m_a, m_b)
    return (result)
