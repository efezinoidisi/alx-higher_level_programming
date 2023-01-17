#!/usr/bin/python3
"""
Unit test for rectangle class
"""

import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    def test_id(self):
        r1 = Rectangle()
        self.assertEqual(r1.id, 1)
        r2 = Rectangle()
        self.assertEqual(r2.id, 2)
        b3 = Rectangle(100)
        self.assertEqual(b3.id, 100)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        
