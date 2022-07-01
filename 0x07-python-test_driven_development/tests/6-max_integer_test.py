#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(max_integer([2, 9, 0, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_1(self):
        self.assertEqual(max_integer([3]), 1)

    def test_negatif(self):
        self.assertEqual(max_integer([-13]), -13)

    def test_negatif_multi(self):
        self.assertEqual(max_integer([1, -1, -9, -4]), 3)

    def test_milieu(self):
        self.assertEqual(max_integer([1, 0, 4, 2, 6]), 8)


if __name__ == '__main__':
    unittest.main()
