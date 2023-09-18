#!/usr/bin/python3
"""unittest for class Square"""
import unittest
from io import StringIO
import sys
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
    Run with python3 -m unittest -v tests/test_models/test_square.py
    """
    s1 = Square(5)
    s2 = Square(2, 2)
    s3 = Square(3, 1, 3)

    def test_square(self):
        self.assertIsInstance(self.s1, Base)
        self.assertIsInstance(self.s2, Rectangle)
        s4 = Square(4, 5, 2)
        self.assertEqual(s4.x, 5)
        s5 = Square(4, 5, 2, 1)
        self.assertEqual(s5.y, 2)
        self.assertEqual(s5.id, 1)
        with self.assertRaises(TypeError):
            Square(7, 8, 4, 2, 5)
        with self.assertRaises(TypeError):
            Square()

    def test_id(self):
        id_1 = int('{}'.format(self.s1.id))
        self.assertEqual(self.s1.id, id_1)
        id_2 = int('{}'.format(self.s2.id))
        self.assertTrue(self.s2.id, id_2)
        id_3 = int('{}'.format(self.s3.id))
        self.assertTrue(self.s3.id, id_3)
        s4 = Square(8, 9, 6, 14)
        self.assertEqual(s4.id, 14)

    def test_get_value(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(self.s1.__size)
        with self.assertRaises(AttributeError):
            print(self.s2.__x)
        with self.assertRaises(AttributeError):
            print(Square(3, 4, 5).__y)

    def test_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.size = -3
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s2.size = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s1.x = -4
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s3.y = -9

    def test_set_values(self):
        s4 = Square(3)
        s4.size = 8
        self.assertTrue(s4.size == 8)
        s4.x = 3
        self.assertTrue(s4.x == 3)
        s4.y = 1
        self.assertTrue(s4.y == 1)

    def test_value_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = 4.0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = True
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = "4"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = (4,)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = [4]
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = {4}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = None
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = 2.0
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = "2"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = {2}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = [2]
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = (2,)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = True
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = None
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = 1.0
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = "1"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = [1]
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = (1,)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = {1}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = True
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = None

    def test_size_value(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("7", 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1: 2, 3: 2}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 3], 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((2, 3), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.0, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(7), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2, 3}, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({2, 3}), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'byte', 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'byte'), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'byte'), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5)

    def test_x_value(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "7")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {1: 2, 3: 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, [2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, (2, 3))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 3.0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, complex(7))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {2, 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, frozenset({2, 3}))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, range(3))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, b'byte')
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, bytearray(b'byte'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, memoryview(b'byte'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('inf'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, float('nan'))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -4)

    def test_y_value(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, "7")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, {1: 2, 3: 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, [2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, (2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, 3.0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, complex(7))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, {2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, frozenset({2, 3}))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, range(3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, b'byte')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, bytearray(b'byte'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, memoryview(b'byte'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 6, float('nan'))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 6, -2)

    def test_value_error_order(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("7", (3,), [2])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((7,), 3, [2])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, [4], {3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, {6})
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, (3,), [2])

    def test_area(self):
        self.assertAlmostEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertTrue(self.s3.area() == 9)
        s4 = Square(8, 9, 6, 14)
        self.assertTrue(s4.area() == 64)
        s5 = Square(99999999999999999999, 2, 1)
        self.assertEqual(9999999999999999999800000000000000000001, s5.area())
        s5.size = 20
        self.assertEqual(s5.area(), 400)
        with self.assertRaises(TypeError):
            s5.size(5)

    def test_print_square(self):
        s4 = Square(8, 9, 6, 14)
        output = '[Square] ({}) 9/6 - 8'.format(s4.id)
        self.assertEqual(s4.__str__(), output)
        output = '[Square] ({}) 0/0 - 5'.format(self.s1.id)
        self.assertEqual(self.s1.__str__(), output)
        output = '[Square] ({}) 2/0 - 2'.format(self.s2.id)
        self.assertEqual(self.s2.__str__(), output)
        output = '[Square] ({}) 1/3 - 3'.format(self.s3.id)
        self.assertEqual(self.s3.__str__(), output)

    def test_print_square_size(self):
        s = Square(4)
        output = '[Square] ({}) 0/0 - 4'.format(s.id)
        self.assertEqual(str(s), output)

    def test_print_square_size_and_x(self):
        s1 = Square(5, 1)
        output = '[Square] ({}) 1/0 - 5'.format(s1.id)
        self.assertEqual(str(s1), output)

    def test_print_square_size_x_and_y(self):
        s2 = Square(8, 3, 2)
        output = '[Square] ({}) 3/2 - 8'.format(s2.id)
        self.assertEqual(s2.__str__(), output)

    def test_print_square_size_x_y_and_id(self):
        s3 = Square(6, 2, 3, 7)
        output = '[Square] ({}) 2/3 - 6'.format(s3.id)
        self.assertEqual(s3.__str__(), output)

    def test_arg_with_str(self):
        with self.assertRaises(TypeError):
            Square(7).__str__(2)

    @staticmethod
    def format_to_stdout(sq):
        """
        Methods to print square to stdout
        Args:
            sq - instances of Square to print
        Return:
            print square in '#' form to stdout'
        """
        store = StringIO()
        sys.stdout = store
        sq.display()
        sys.stdout = sys.__stdout__
        return store

    def test_display_1_arg(self):
        s = Square(5)
        output = '#####\n#####\n#####\n#####\n#####\n'
        store = self.format_to_stdout(s)
        self.assertEqual(store.getvalue(), output)

    def test_display_2_args(self):
        s1 = Square(3, 2)
        output = '  ###\n  ###\n  ###\n'
        store = self.format_to_stdout(s1)
        self.assertEqual(store.getvalue(), output)

    def test_display_3_args(self):
        s2 = Square(3, 1, 2)
        output = '\n\n ###\n ###\n ###\n'
        store = self.format_to_stdout(s2)
        self.assertEqual(store.getvalue(), output)

    def test_display_4_args(self):
        s3 = Square(4, 0, 3, 6)
        output = '\n\n\n####\n####\n####\n####\n'
        store = self.format_to_stdout(s3)
        self.assertEqual(store.getvalue(), output)

    def test_arg_into_display(self):
        with self.assertRaises(TypeError):
            Square(5).display(1)

    def test_update_args(self):
        s5 = Square(6, 3, 1, 5)
        s5.update()
        self.assertEqual(str(s5), '[Square] (5) 3/1 - 6')
        s5.update(89)
        self.assertEqual(str(s5), '[Square] (89) 3/1 - 6')
        s5.update(89, 16)
        self.assertEqual(str(s5), '[Square] (89) 3/1 - 16')
        s5.update(89, 16, 6)
        self.assertEqual(str(s5), '[Square] (89) 6/1 - 16')
        s5.update(89, 16, 6, 3)
        self.assertEqual(str(s5), '[Square] (89) 6/3 - 16')
        s5.update(89, 16, 6, 3, 2)
        self.assertEqual(str(s5), '[Square] (89) 6/3 - 16')
        s5.update(1, 2, 3, 4)
        s5.update(4, 3, 2, 1)
        self.assertEqual(str(s5), '[Square] (4) 2/1 - 3')

    def test_update_args_error(self):
        s5 = Square(6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s5.update(5, "7")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s5.update(7, (6,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5.update(7, 6, [2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s5.update(7, 6, 2, {3})
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5.update(7, 0, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5.update(7, -1, 4, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s5.update(7, 4, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s5.update(7, 4, 3, -3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s5.update(7, (3,), [2], {6})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5.update(7, 3, {2}, [3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s5.update(7, 3, 6, "5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5.update(7, 0, (3,), [2])

    def test_update_kwargs(self):
        s5 = Square(6, 3, 1, 5)
        s5.update(size=6)
        self.assertEqual(str(s5), '[Square] (5) 3/1 - 6')
        s5.update(siz=6, x=1)
        self.assertEqual(str(s5), '[Square] (5) 1/1 - 6')
        s5.update(y=3, size=6, x=1)
        self.assertEqual(str(s5), '[Square] (5) 1/3 - 6')
        s5.update(id=89, size=6, x=1, y=3)
        self.assertEqual(str(s5), '[Square] (89) 1/3 - 6')
        s = Square(5, 4, 2, 1)
        s.update(x=3, size=5, y=2)
        s.update(x=5, size=6, y=1)
        self.assertEqual(str(s), '[Square] (1) 5/1 - 6')

    def test_update_kwargs_error(self):
        s5 = Square(6, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s5.update(size={2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5.update(x=[2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s5.update(y="3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5.update(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s5.update(size=-7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s5.update(x=-4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s5.update(y=-3)

    def test_args_and_kwargs(self):
        s = Square(5, 3)
        s.update(6, 5, x=1, y=3, size=4)
        self.assertEqual(str(s), '[Square] (6) 3/0 - 5')
        s.update(p=2, q=3)
        self.assertEqual(str(s), '[Square] (6) 3/0 - 5')
        s.update(p=2, size=12, id=89, q=3, x=1, y=3)
        self.assertEqual(str(s), '[Square] (89) 1/3 - 12')

    def test_to_dictionary(self):
        s6 = Square(10, 2, 1, 6)
        s6_dict = {'id': 6, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s6.to_dictionary(), s6_dict)
        s = Square(1, 2, 3, 4)
        s.update(**s6.to_dictionary())
        self.assertNotEqual(s6, s)
        with self.assertRaises(TypeError):
            s6.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
