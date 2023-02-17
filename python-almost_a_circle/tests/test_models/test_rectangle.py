#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle
from models.base import Base

from io import StringIO
from contextlib import redirect_stdout


"""rectangle test"""


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        elf.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_type_error_init(self):
        self.assertRaisesRegex(TypeError, "width must be an integer",
                Rectangle, "8", 6, 4, 2, 10)
        self.assertRaisesRegex(TypeError, "height must be an integer",
                Rectangle, 8, "6", 4, 2, 10)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                Rectangle, 8, 6, "4", 2, 10)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                Rectangle, 8, 6, 4, "2", 10)

    def test_value_error_init(self):
        self.assertRaisesRegex(ValueError, "width must be > 0",
                Rectangle, -8, 6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                Rectangle, 0, 6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                Rectangle, 2, 0, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                Rectangle, 8, -6, 4, 2, 10)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                Rectangle, 8, 6, -4, 2, 10)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                Rectangle, 8, 6, 4, -2, 10)

    def test_width_positive_integer(self):
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_width_not_integer(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "not an integer"

    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

        r = Rectangle(5, 7)
        self.assertEqual(r.area(), 35)

    def test_display(self):
        r1 = Rectangle(3, 2)
        expected_output = '###\n###\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r2 = Rectangle(2, 3)
        expected_output = '##\n##\n##\n'
        with StringIO() as buffer, redirect_stdout(buffer):
            r2.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

    def test_str(self):
        r = Rectangle(14, 16, 12, 15, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 12/15 - 14/16")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 20)
        self.assertEqual(r.width, 20)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_to_dictionary(self):
        r = Rectangle(2, 4, 6, 8, 22)
        self.assertEqual(r.to_dictionary(), {'id': 22, 'width': 2,
            'height': 4, 'x': 6, 'y': 8})

    def test_create(self):
        r = Rectangle.create(**{'id': 1, 'width': 3,'height': 5,
            'x': 0, 'y': 0})
        r1 = Rectangle(1, 3, 5)
        self.assertIsNot(r, r1)

    def test_save_to_file(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            read = f.read()
        self.assertEqual(read, '[]')

        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            read = f.read()
        result = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(read, result)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            read = f.read()
        self.assertEqual(read, '[]')

    def test_load_from_file(self):
        r = Rectangle(5, 8)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].width, 5)
        self.assertEqual(rectangles[0].height, 8)

if __name__ == '__main__':
    unittest.main()
