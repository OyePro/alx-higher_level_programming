#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[0, 2], [5, 4]], [[-1, 2], [3, 8]]))
print(matrix_mul([[0, -2], [-5.0, 4]], [[-1.4, 2], [-3.5, 8]]))

try:
    print(matrix_mul([[1, 2.0]], [[3, 4], [5, 6]]))
except Exception as e:
    print(e)
