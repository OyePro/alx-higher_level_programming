#!/usr/bin/python3
"""defining a function print_square"""


def print_square(size):
    """
    Return square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    print("\n".join(["#" * size for rows in range(size)]))
