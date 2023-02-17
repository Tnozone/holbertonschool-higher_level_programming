import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout


"""square test"""


class TestSquare(unittest.TestCase):
    def test_attributes(self):
        s1 = Square(5, 2, 3, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 10)

    def test_str(self):
        s1 = Square(5, 2, 3, 10)
        self.assertEqual(str(s1), "[Square] (10) 2/3 - 5")

    def test_update_args(self):
        s1 = Square(5, 2, 3, 10)
        s1.update(11, 7, 8, 9)
        self.assertEqual(s1.id, 11)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_update_kwargs(self):
        s1 = Square(5, 2, 3, 10)
        s1.update(id=11, size=7, x=8, y=9)
        self.assertEqual(s1.id, 11)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_to_dictionary(self):
        s1 = Square(5, 2, 3, 10)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s1_dict, expected_dict)
