#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    """run test with python3 -m unittest -v tests.6-max_integer_test"""

    def test_max_integer(self):
        self.assertEqual(max_integer([2, 9, 6, 8]), 9)
        self.assertEqual(max_integer([3, 7, 3, 12]), 12)
        self.assertEqual(max_integer([0, 4, -3, -1]), 4)
        self.assertEqual(max_integer([-2, -9, -6, -8]), -2)

    def test_max_float(self):
        self.assertEqual(max_integer([2.0, 9.0, 6.5, 9.1]), 9.1)
        self.assertEqual(max_integer([3.4, 7.2, 3.1, -12.8]), 7.2)
        self.assertEqual(max_integer([0.7, -4.6, -3.5, -1.3]), 0.7)
        self.assertEqual(max_integer([-2.98, -9.54, -6.32, -8.13]), -2.98)

    def test_max_strings(self):
        self.assertEqual(max_integer("4561"), '6')
        self.assertEqual(max_integer("axvw"), 'x')
        self.assertEqual(max_integer(["4", "5", "6", "7"]), '7')
        self.assertEqual(max_integer(["a", "c", "y", "r"]), 'y')
        self.assertEqual(max_integer(["acd", "z"]), 'z')

    def test_max_lists_tuples(self):
        self.assertEqual(max_integer([[1, 5], [2, 5]]), [2, 5])
        self.assertEqual(max_integer([(1, 5), (2, 5)]), (2, 5))
        self.assertEqual(max_integer(([1, 5], [2, 5])), [2, 5])
        self.assertEqual(max_integer(((1, 5), (2, 5))), (2, 5))

    def test_value(self):
        with self.assertRaises(TypeError):
            max_integer({1, 3}, {1, 4, 5})
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([1, "n", 1.8])
        with self.assertRaises(TypeError):
            max_integer([False, None])

    def test_bool(self):
        self.assertEqual(max_integer([True, False]), True)


if __name__ == "__main__":
    unittest.main()
