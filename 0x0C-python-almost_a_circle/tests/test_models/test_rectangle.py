#!/usr/bin/python3
"""unittest for class Rectangle"""
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    Run with python3 -m unittest -v tests/test_models/test_rectangle.py
    """

    r1 = Rectangle(7, 8)
    r2 = Rectangle(10, 2)
    r3 = Rectangle(6, 4, 0, 0, 12)

    def test_Rectangle(self):
        self.assertIsInstance(self.r1, Base)
        r4 = Rectangle(4, 5, 2)
        self.assertEqual(r4.x, 2)
        r5 = Rectangle(4, 5, 2, 1)
        self.assertEqual(r5.y, 1)
        r6 = Rectangle(4, 5, 2, 1, 89)
        self.assertEqual(r6.id, 89)
        with self.assertRaises(TypeError):
            Rectangle(7, 8, 4, 2, 5, 7)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(9)

    def test_id(self):
        id_1 = '{}'.format(self.r1.id)
        self.assertEqual(self.r1.id, int(id_1))
        id_2 = '{}'.format(self.r2.id)
        self.assertEqual(self.r2.id, int(id_2))
        self.assertEqual(self.r3.id, 12)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(self.r1.__width)
        with self.assertRaises(AttributeError):
            print(self.r2.__height)
        with self.assertRaises(AttributeError):
            print(self.r3.__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 4, 5, 1, 6).__y)

    def test_get_values(self):
        self.assertEqual(self.r1.width, 7)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r1.y, 0)
        r4 = Rectangle(2, 3, 1, 2)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 2)

    def test_values(self):
        with self.assertRaises(ValueError):
            self.r1.width = -10
        with self.assertRaises(ValueError):
            self.r2.width = 0
        with self.assertRaises(ValueError):
            self.r3.height = -4
        with self.assertRaises(ValueError):
            self.r1.height = 0
        with self.assertRaises(ValueError):
            self.r1.x = -8
        with self.assertRaises(ValueError):
            self.r1.y = -2

    def test_set_value(self):
        r8 = Rectangle(3, 4)
        r8.width = 5
        self.assertTrue(r8.width == 5)
        r8.height = 7
        self.assertTrue(r8.height == 7)
        r8.x = 2
        self.assertEqual(r8.x, 2)
        r8.y = 1
        self.assertEqual(r8.y, 1)

    def test_values_type(self):
        with self.assertRaises(TypeError):
            self.r1.width = "2"
        with self.assertRaises(TypeError):
            self.r1.width = 2.0
        with self.assertRaises(TypeError):
            self.r1.width = (2,)
        with self.assertRaises(TypeError):
            self.r1.width = [2]
        with self.assertRaises(TypeError):
            self.r1.width = {2}
        with self.assertRaises(TypeError):
            self.r1.width = False
        with self.assertRaises(TypeError):
            self.r1.width = None
        with self.assertRaises(TypeError):
            self.r1.height = False
        with self.assertRaises(TypeError):
            self.r1.height = None
        with self.assertRaises(TypeError):
            self.r1.height = "5"
        with self.assertRaises(TypeError):
            self.r1.height = 5.0
        with self.assertRaises(TypeError):
            self.r1.height = (5,)
        with self.assertRaises(TypeError):
            self.r1.height = [5]
        with self.assertRaises(TypeError):
            self.r1.width = {5}
        with self.assertRaises(TypeError):
            self.r1.x = "1"
        with self.assertRaises(TypeError):
            self.r1.x = 1.0
        with self.assertRaises(TypeError):
            self.r1.x = (1,)
        with self.assertRaises(TypeError):
            self.r1.x = [1]
        with self.assertRaises(TypeError):
            self.r1.x = {1}
        with self.assertRaises(TypeError):
            self.r1.x = True
        with self.assertRaises(TypeError):
            self.r1.x = None
        with self.assertRaises(TypeError):
            self.r1.y = "3"
        with self.assertRaises(TypeError):
            self.r1.y = 3.0
        with self.assertRaises(TypeError):
            self.r1.y = (3,)
        with self.assertRaises(TypeError):
            self.r1.y = [3]
        with self.assertRaises(TypeError):
            self.r1.y = {3}
        with self.assertRaises(TypeError):
            self.r1.y = True
        with self.assertRaises(TypeError):
            self.r1.y = None

    def test_width_value(self):
        with self.assertRaises(TypeError):
            Rectangle("7", 5)
        with self.assertRaises(TypeError):
            Rectangle({1: 2, 3: 2}, 5)
        with self.assertRaises(TypeError):
            Rectangle([2, 3], 5)
        with self.assertRaises(TypeError):
            Rectangle((2, 3), 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 5)
        with self.assertRaises(TypeError):
            Rectangle(False, 5)
        with self.assertRaises(TypeError):
            Rectangle(3.0, 5)
        with self.assertRaises(TypeError):
            Rectangle(complex(7), 5)
        with self.assertRaises(TypeError):
            Rectangle({2, 3}, 5)
        with self.assertRaises(TypeError):
            Rectangle(frozenset({2, 3}), 5)
        with self.assertRaises(TypeError):
            Rectangle(range(3), 5)
        with self.assertRaises(TypeError):
            Rectangle(b'byte', 5)
        with self.assertRaises(TypeError):
            Rectangle(bytearray(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(memoryview(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 5)
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 5)
        with self.assertRaises(ValueError):
            Rectangle(-4, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_height_value(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "7")
        with self.assertRaises(TypeError):
            Rectangle(3, {1: 2, 3: 2})
        with self.assertRaises(TypeError):
            Rectangle(3, [2, 3])
        with self.assertRaises(TypeError):
            Rectangle(3, (2, 3))
        with self.assertRaises(TypeError):
            Rectangle(3, None)
        with self.assertRaises(TypeError):
            Rectangle(3, False)
        with self.assertRaises(TypeError):
            Rectangle(3, 3.0)
        with self.assertRaises(TypeError):
            Rectangle(3, complex(7))
        with self.assertRaises(TypeError):
            Rectangle(3, {2, 3})
        with self.assertRaises(TypeError):
            Rectangle(3, frozenset({2, 3}))
        with self.assertRaises(TypeError):
            Rectangle(3, range(3))
        with self.assertRaises(TypeError):
            Rectangle(3, b'byte')
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'byte'), 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, memoryview(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(3, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(3, float('nan'))
        with self.assertRaises(ValueError):
            Rectangle(3, -4)
        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_x_value(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 6, "7")
        with self.assertRaises(TypeError):
            Rectangle(3, 6, {1: 2, 3: 2})
        with self.assertRaises(TypeError):
            Rectangle(3, 6, [2, 3])
        with self.assertRaises(TypeError):
            Rectangle(3, 6, (2, 3))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, None)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, False)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 3.0)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, complex(7))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, {2, 3})
        with self.assertRaises(TypeError):
            Rectangle(3, 6, frozenset({2, 3}))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, range(3))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, b'byte')
        with self.assertRaises(TypeError):
            Rectangle(3, 6, bytearray(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, memoryview(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, float('nan'))
        with self.assertRaises(ValueError):
            Rectangle(3, 6, -4)

    def test_y_value(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, "7")
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, {1: 2, 3: 2})
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, [2, 3])
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, (2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 6, 2, None)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, False)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, 3.0)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, complex(7))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, {2, 3})
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, frozenset({2, 3}))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, range(3))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, b'byte')
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, bytearray(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, memoryview(b'byte'), 5)
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(3, 6, 2, float('nan'))
        with self.assertRaises(ValueError):
            Rectangle(3, 6, 2, -4)

    def test_value_error_order(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("7", (3,), [2], {6})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (3,), [2], {1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 3, [4], {2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 3, 2, {6})
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, (3,), [2], {1})

    def test_area(self):
        self.assertAlmostEqual(self.r1.area(), 56)
        self.assertEqual(self.r2.area(), 20)
        self.assertAlmostEqual(self.r3.area(), 24)
        r5 = Rectangle(999999999999999, 99999999999999999, 2, 3, 13)
        self.assertAlmostEqual(r5.area(), 99999999999999899000000000000001)
        r5.width = 10
        r5.height = 15
        self.assertEqual(r5.area(), 150)
        with self.assertRaises(TypeError):
            r5.area(6)

    def test_print_rect(self):
        r4 = Rectangle(4, 6, 2, 1, 89)
        self.assertEqual(r4.__str__(), '[Rectangle] (89) 2/1 - 4/6')
        self.assertEqual(self.r1.__str__(), '[Rectangle] (1) 0/0 - 7/8')
        self.assertEqual(self.r2.__str__(), '[Rectangle] (2) 0/0 - 10/2')
        self.assertEqual(self.r3.__str__(), '[Rectangle] (12) 0/0 - 6/4')

    def test_print_rect_width_and_height(self):
        r = Rectangle(4, 2)
        output = '[Rectangle] ({}) 0/0 - 4/2'.format(r.id)
        self.assertEqual(str(r), output)

    def test_print_rect_width_height_and_x(self):
        r1 = Rectangle(5, 4, 1)
        output = '[Rectangle] ({}) 1/0 - 5/4'.format(r1.id)
        self.assertEqual(str(r1), output)

    def test_print_rect_width_height_x_and_y(self):
        r2 = Rectangle(8, 9, 2, 3)
        output = '[Rectangle] ({}) 2/3 - 8/9'.format(r2.id)
        self.assertEqual(r2.__str__(), output)

    def test_print_rect_width_height_x_y_and_id(self):
        r3 = Rectangle(6, 7, 3, 2, 4)
        output = '[Rectangle] ({}) 3/2 - 6/7'.format(r3.id)
        self.assertEqual(str(r3), output)

    def test_print_rect_arg(self):
        r3 = Rectangle(6, 7, 3, 2, 4)
        with self.assertRaises(TypeError):
            r3.__str__(2)

    @staticmethod
    def format_to_stdout(rect):
        """
        Methods to print rectangle to stdout
        Args:
            rect - instances of Rectangle to print
        Return:
            print rectangle in '#' form'
        """
        store = StringIO()
        sys.stdout = store
        rect.display()
        sys.stdout = sys.__stdout__
        return store

    def test_display_rect_2_args(self):
        r = Rectangle(4, 2)
        output = '####\n####\n'
        store = self.format_to_stdout(r)
        self.assertEqual(store.getvalue(), output)

    def test_display_rect_3_args(self):
        r1 = Rectangle(6, 4, 2)
        output = '  ######\n  ######\n  ######\n  ######\n'
        store = self.format_to_stdout(r1)
        self.assertEqual(store.getvalue(), output)

    def test_display_rect_4_args(self):
        r2 = Rectangle(3, 2, 1, 2)
        output = '\n\n ###\n ###\n'
        store = self.format_to_stdout(r2)
        self.assertEqual(store.getvalue(), output)

    def test_display_rect_5_args(self):
        r3 = Rectangle(10, 2, 0, 1, 89)
        output = '\n##########\n##########\n'
        store = self.format_to_stdout(r3)
        self.assertEqual(store.getvalue(), output)

    def test_arg_into_display(self):
        r3 = Rectangle(10, 2, 0, 1, 89)
        with self.assertRaises(TypeError):
            r3.display(1)

    def test_update_args(self):
        r5 = Rectangle(6, 12, 3, 1, 5)
        r5.update()
        self.assertEqual(str(r5), '[Rectangle] (5) 3/1 - 6/12')
        r5.update(89)
        self.assertEqual(str(r5), '[Rectangle] (89) 3/1 - 6/12')
        r5.update(89, 16)
        self.assertEqual(str(r5), '[Rectangle] (89) 3/1 - 16/12')
        r5.update(89, 16, 24)
        self.assertEqual(str(r5), '[Rectangle] (89) 3/1 - 16/24')
        r5.update(89, 16, 24, 6)
        self.assertEqual(str(r5), '[Rectangle] (89) 6/1 - 16/24')
        r5.update(89, 16, 24, 6, 2)
        self.assertEqual(str(r5), '[Rectangle] (89) 6/2 - 16/24')
        r5.update(89, 16, 24, 6, 2, 1)
        self.assertEqual(str(r5), '[Rectangle] (89) 6/2 - 16/24')
        r5.update(1, 2, 3, 4, 5)
        r5.update(5, 4, 3, 2, 1)
        self.assertEqual(str(r5), '[Rectangle] (5) 2/1 - 4/3')

    def test_update_args_error(self):
        r5 = Rectangle(7, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5.update(5, "7")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5.update(7, 6, (7,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5.update(7, 6, 3, [2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5.update(7, 6, 3, 2, {3})
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5.update(7, 0, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5.update(7, -1, 4, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5.update(7, 4, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5.update(7, 4, -1, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5.update(7, 4, 3, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5.update(7, 4, 3, 2, -3)

    def test_update_args_error_order(self):
        r5 = Rectangle(6, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5.update(7, (3,), [2], {6}, "5")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5.update(7, 3, [2], {1}, "5")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5.update(7, 3, 4, {2}, [3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5.update(7, 3, 2, 6, "5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5.update(7, 0, (3,), [2], {1})

    def test_update_kwargs(self):
        r5 = Rectangle(6, 12, 3, 1, 5)
        r5.update(height=6)
        self.assertEqual(str(r5), '[Rectangle] (5) 3/1 - 6/6')
        r5.update(height=6, x=1)
        self.assertEqual(str(r5), '[Rectangle] (5) 1/1 - 6/6')
        r5.update(y=3, height=6, x=1)
        self.assertEqual(str(r5), '[Rectangle] (5) 1/3 - 6/6')
        r5.update(id=89, height=6, x=1, y=3)
        self.assertEqual(str(r5), '[Rectangle] (89) 1/3 - 6/6')
        r5.update(width=12, id=89, height=6, x=1, y=3)
        self.assertEqual(str(r5), '[Rectangle] (89) 1/3 - 12/6')
        r = Rectangle(5, 3, 4, 2, 1)
        r.update(x=3, width=5, y=2)
        r.update(x=5, width=6, y=1)
        self.assertEqual(str(r), '[Rectangle] (1) 5/1 - 6/3')

    def test_update_kwargs_error(self):
        r5 = Rectangle(4, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5.update(width={2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5.update(height=(7,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5.update(x=[2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5.update(y="3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5.update(width=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5.update(width=-7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5.update(height=0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5.update(height=-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5.update(x=-4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5.update(y=-3)

    def test_args_and_kwargs(self):
        r = Rectangle(5, 3, 4, 2, 1)
        r.update(6, 5, x=1, y=3, width=4)
        self.assertEqual(str(r), '[Rectangle] (6) 4/2 - 5/3')
        r.update(p=2, q=3)
        self.assertEqual(str(r), '[Rectangle] (6) 4/2 - 5/3')
        r.update(p=2, width=12, id=89, q=3, height=6, x=1, y=3)
        self.assertEqual(str(r), '[Rectangle] (89) 1/3 - 12/6')

    def test_to_dictionary(self):
        r = Rectangle(9, 2, 1, 9, 11)
        r_dict = {'id': 11, 'width': 9, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), r_dict)
        r1 = Rectangle(5, 4, 3, 1, 2)
        r1.update(**r.to_dictionary())
        self.assertNotEqual(r1, r)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
