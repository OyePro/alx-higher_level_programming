#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
try:
    print(lazy_matrix_mul(([{1, 2}]), [[3, 4], [5, 6]]))
except Exception as e:
    print(e)
m_a = [[1, 2], [3, 4, 5]]
m_b = [[1, 2], [3, 4]]
print(lazy_matrix_mul(m_a, m_b))