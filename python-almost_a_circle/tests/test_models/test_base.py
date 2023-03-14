#!/usr/bin/python3


"""unitest for Base"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Unitest for class Base"""

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(22)
        self.assertEqual(b3.id, 22)

        b4 = Base(20)
        self.assertEqual(b4.id, 20)

        b5 = Base(50)
        self.assertEqual(b5.id, 50)

if __name__ == '__main__':
    unittest.main()
