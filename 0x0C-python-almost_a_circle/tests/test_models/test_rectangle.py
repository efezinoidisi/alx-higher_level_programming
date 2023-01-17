#!/usr/bin/python3
"""
Unit test for rectangle class
"""

import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    def test_width(self):
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.width, 10)
        
