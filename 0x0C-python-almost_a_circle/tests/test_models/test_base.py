#!/usr/bin/python3
"""
Unit test for the Base class in the base module
"""

import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        
if __name__ == "__main__":
    unittest.main()
