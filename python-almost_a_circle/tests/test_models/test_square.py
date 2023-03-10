#!/usr/bin/python3


"""square test"""


import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(8, 6, 4, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 4)

    def test_type_error_init(self):
        self.assertRaisesRegex(TypeError, "width must be an integer",
                Square, "6", 4, 2, 10)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                Square, 6, "4", 2, 10)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                Square, 6, 4, "2", 10)

    def test_value_error_init(self):
        self.assertRaisesRegex(ValueError, "width must be > 0",
                Square, -8, 6, 4, 10)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                Square, 0, 6, 4, 10)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                Square, 8, -6, 2, 10)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                Square, 8, 6, -2, 10)

    def test_area(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(8, 0, 0, 12)
        self.assertEqual(s2.area(), 64)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_display(self):
        s = Square(4)
        output = '####\n####\n####\n####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

        s1 = Square(5, 1, 1)
        output = '\n #####\n #####\n #####\n #####\n #####\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            s1.display()
            res = buffer.getvalue()
        self.assertEqual(res, output)

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 20)
        self.assertEqual(s.size, 20)

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1)
        self.assertEqual(s.size, 1)

    def test_to_dictionary(self):
        s = Square(4, 6, 8, 22)
        self.assertEqual(s.to_dictionary(), {'id': 22, 'size': 4,
            'x': 6, 'y': 8})

    def test_create(self):
        s = Square.create(**{'id': 5, 'size': 6,'x': 2, 'y': 1})
        s1 = Square(6, 2, 1, 5)
        self.assertIsNot(s, s1)

    def test_save_to_file(self):
        s = Square(10, 2, 8, 1)
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            read = f.read()
        self.assertEqual(read, '[]')

        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            read = f.read()
        result = '[{"size": 10, "x": 2, "y": 8, "id": 1}]'
        self.assertEqual(read, result)

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            read = f.read()
        self.assertEqual(read, '[]')

    def test_load_from_file(self):
        s = Square(5)
        Square.save_to_file([s])
        Squares = Square.load_from_file()
        self.assertIsInstance(Squares[0], Square)
        self.assertEqual(Squares[0].size, 5)

if __name__ == '__main__':
    unittest.main()
