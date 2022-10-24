#!/usr/bin/python3
"""unittest for class Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Run with python3 -m unittest -v tests/test_models/test_base.py
    """
    def test_id(self):
        b = Base()
        id_1 = int('{}'.format(b.id))
        self.assertEqual(b.id, id_1)
        b = Base(4)
        self.assertEqual(b.id, 4)

    def test_2_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_3_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b1.id + 1)

    def test_instances(self):
        b1 = Base()
        b2 = Base(8)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)
        self.assertEqual(b2.id, 8)

    def test_id_with_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_set_id(self):
        b3 = Base(7)
        b3.id = 2
        self.assertEqual(b3.id, 2)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            Base(12).__nb_objects

    def test_id_with_other_types(self):
        self.assertEqual(Base("7").id, '7')
        self.assertEqual(Base((2, 3)).id, (2, 3))
        self.assertEqual(Base([2, 3]).id, [2, 3])
        self.assertEqual(Base({2, 3}).id, {2, 3})
        self.assertEqual(Base({1: 2, 3: 4}).id, {1: 2, 3: 4})
        self.assertEqual(Base(6.5).id, 6.5)
        self.assertEqual(Base(True).id, True)
        self.assertEqual(Base(frozenset({1, 2})).id, frozenset({1, 2}))
        self.assertEqual(Base(complex(7)).id, complex(7))
        self.assertEqual(Base(range(7)).id, range(7))
        self.assertEqual(Base(b'byte').id, b'byte')
        self.assertEqual(Base(bytearray(b'byte')).id, bytearray(b'byte'))
        self.assertEqual(Base(memoryview(b'byte')).id, memoryview(b'byte'))
        self.assertEqual(Base(float('inf')).id, float('inf'))
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(2, 3)

    def test_to_json_string_rect(self):
        r1 = Rectangle(8, 7, 3, 2, 9)
        r2 = Rectangle(9, 10, 6, 5, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_dicts = Base.to_json_string(list_dicts)
        self.assertIs(str, type(json_dicts))
        r = Rectangle(4, 5, 3, 8, 2)
        list_dict = [r.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 52)
        r3 = Rectangle(8, 7, 3, 2, 9)
        list_dict = [r3.to_dictionary()]
        self.assertIs(str, type(Base.to_json_string(list_dict)))

    def test_to_json_string_sq(self):
        s1 = Square(7, 3, 4, 2)
        s2 = Square(9, 8, 5, 6)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        json_dicts = Base.to_json_string(list_dicts)
        self.assertEqual(str, type(json_dicts))
        self.assertNotEqual(type(list_dicts), type(json_dicts))
        s = Square(7, 8, 3, 2)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 38)
        s3 = Square(8, 2, 3, 89)
        self.assertEqual(str, type(Base.to_json_string([s3.to_dictionary()])))

    def test_to_json_string_empty_and_None(self):
        self.assertEqual(Base.to_json_string([]), '"[]"')
        self.assertEqual(Base.to_json_string(None), '"[]"')

    def test_to_json_string_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_from_json_string_rect(self):
        r1 = Rectangle(8, 7, 3, 2, 9)
        r2 = Rectangle(9, 10, 6, 5, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_dicts = Base.to_json_string(list_dicts)
        self.assertEqual(list, type(Base.from_json_string(json_dicts)))
        self.assertEqual(list_dicts, Base.from_json_string(json_dicts))
        r = Rectangle(4, 5, 3, 8, 2)
        list_dict = [r.to_dictionary()]
        json_dict = Base.to_json_string(list_dict)
        self.assertEqual(list_dict, Base.from_json_string(json_dict))

    def test_from_json_string_sq(self):
        s1 = Square(7, 3, 4, 2)
        s2 = Square(9, 8, 5, 6)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        json_dicts = Base.to_json_string(list_dicts)
        self.assertEqual(list, type(Base.from_json_string(json_dicts)))
        self.assertEqual(list_dicts, Base.from_json_string(json_dicts))
        s = Square(8, 6, 5, 3)
        list_dict = [s.to_dictionary()]
        json_dict = Base.to_json_string(list_dict)
        self.assertEqual(list_dict, Base.from_json_string(json_dict))

    def test_from_json_string_empty_and_None(self):
        self.assertEqual('"[]"', Base.from_json_string(None))
        self.assertEqual('"[]"', Base.from_json_string(json_string=""))

    def test_from_json_string_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string("p", "I")

    def test_save_to_file_rect(self):
        r1 = Rectangle(8, 9, 7, 4, 10)
        r2 = Rectangle(6, 5, 7, 4, 11)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as fp:
            self.assertEqual(106, len(fp.read()))
        r = Rectangle(8, 6, 4, 1, 9)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as fp:
            self.assertEqual(52, len(fp.read()))

    def test_save_to_file_sq(self):
        s1 = Square(12, 5, 3, 89)
        s2 = Square(11, 6, 3, 90)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as fp:
            self.assertEqual(80, len(fp.read()))
        s = Square(9, 7, 3, 8)
        Square.save_to_file([s])
        with open("Square.json", 'r') as fp:
            self.assertEqual(len(fp.read()), 38)

    def test_save_to_file_overwrite(self):
        s = Square(4, 5, 3, 6)
        Square.save_to_file([s])
        s = Square(7, 5, 3, 11)
        Square.save_to_file([s])
        with open("Square.json", 'r') as fp:
            self.assertEqual(39, len(fp.read()))

    def test_save_to_file_None_and_arg(self):
        Square.save_to_file(None)
        with open("Square.json", 'r') as fp:
            self.assertEqual('"[]"', fp.read())
        with self.assertRaises(TypeError):
            Square.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

    def test_rect_sq_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", 'r') as fsq:
            self.assertEqual('"[]"', fsq.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as frect:
            self.assertEqual('"[]"', frect.read())

    def test_load_from_file_rect(self):
        r1 = Rectangle(8, 9, 7, 4, 10)
        r2 = Rectangle(6, 5, 7, 4, 11)
        lists = [r1, r2]
        Rectangle.save_to_file(lists)
        list_output = Rectangle.load_from_file()
        self.assertEqual(type(lists), type(list_output))
        self.assertEqual(str(r1), str(list_output[0]))
        r3 = Rectangle(7, 4, 3, 2, 8)
        r4 = Rectangle(8, 3, 4, 2, 1)
        lists = [r3, r4]
        Rectangle.save_to_file(lists)
        list_output = Rectangle.load_from_file()
        self.assertEqual(type(lists), type(list_output))
        self.assertEqual(str(r4), str(list_output[1]))
        for rect in list_output:
            self.assertEqual(type(rect), Rectangle)

    def test_load_from_file_sq(self):
        s1 = Square(6, 5, 3, 2)
        s2 = Square(5, 4, 2, 1)
        lists = [s1, s2]
        Square.save_to_file(lists)
        list_output = Square.load_from_file()
        self.assertEqual(type(lists), type(list_output))
        self.assertEqual(str(s1), str(list_output[0]))
        self.assertEqual(str(s2), str(list_output[1]))
        for sq in list_output:
            self.assertEqual(type(sq), Square)

    def test_load_from_file_None_and_args(self):
        Square.save_to_file(None)
        None_out = Square.load_from_file()
        self.assertEqual([], None_out)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(2)

    def test_create_rectangle(self):
        r1 = Rectangle(6, 4, 2, 1, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (9) 2/1 - 6/4", str(r1))
        self.assertEqual("[Rectangle] (9) 2/1 - 6/4", str(r2))
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertFalse(r1 == r2)

    def test_create_square(self):
        s1 = Square(5, 3, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual("[Square] (7) 3/2 - 5", str(s1))
        self.assertEqual("[Square] (7) 3/2 - 5", str(s2))
        self.assertEqual(str(s1), str(s1))
        self.assertFalse(s2 == s1)
        self.assertIsNot(s1, s2)

    def test_save_to_file_csv_rect(self):
        r1 = Rectangle(8, 6, 3, 2, 9)
        r2 = Rectangle(7, 5, 3, 2, 7)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", 'r') as fp:
            self.assertEqual('9,8,6,3,2\n7,7,5,3,2\n', fp.read())
        r = Rectangle(6, 4, 5, 2, 8)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", 'r') as fp:
            self.assertEqual('8,6,4,5,2\n', fp.read())

    def test_save_to_file_csv_sq(self):
        s1 = Square(8, 5, 2, 4)
        s2 = Square(6, 4, 3, 1)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", 'r') as fp:
            self.assertEqual('4,8,5,2\n1,6,4,3\n', fp.read())
        s = Square(11, 3, 2, 89)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as fp:
            self.assertEqual('89,11,3,2\n', fp.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(5, 6, 2, 4)
        Square.save_to_file_csv([s])
        s = Square(9, 6, 4, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as fp:
            self.assertEqual('8,9,6,4\n', fp.read())

    def test_save_to_file_csv_empty_and_args(self):
        Square.save_to_file_csv([])
        with open("Square.csv", 'r') as fp:
            self.assertNotEqual('[]', fp.read())
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], [])

    def test_load_from_csv_rect(self):
        r1 = Rectangle(8, 6, 3, 2, 9)
        r2 = Rectangle(7, 5, 3, 2, 7)
        lists = [r1, r2]
        Rectangle.save_to_file_csv(lists)
        load_csv = Rectangle.load_from_file_csv()
        self.assertEqual(type(lists), type(load_csv))
        self.assertEqual(str(r2), str(load_csv[1]))
        for rect in load_csv:
            self.assertEqual(type(rect), Rectangle)
        r = Rectangle(6, 5, 3, 2, 7)
        lists = [r]
        Rectangle.save_to_file_csv(lists)
        load_csv = Rectangle.load_from_file_csv()
        self.assertEqual(str(r), str(load_csv[0]))

    def test_load_from_csv_sq(self):
        s1 = Square(6, 5, 3, 2)
        s2 = Square(5, 4, 2, 1)
        lists = [s1, s2]
        Square.save_to_file_csv(lists)
        load_csv = Square.load_from_file_csv()
        self.assertEqual(type(lists), type(load_csv))
        self.assertEqual(str(s1), str(load_csv[0]))
        self.assertEqual(str(s2), str(load_csv[1]))
        for sq in load_csv:
            self.assertEqual(type(sq), Square)

    def test_load_from_csv_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv(9)


if __name__ == "__main__":
    unittest.main()
