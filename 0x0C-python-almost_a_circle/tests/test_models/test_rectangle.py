#!/usr/bin/python3
"""
Unit test for rectangle class
"""

import unittest
import unittest.mock
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    def test_instance_attributes(self):
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 3)
        r2 = Rectangle(10, 2, 4, 3, 12)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 12)

    def test_validate_instance_attributes(self):
        #test width type and value
        with self.assertRaises(TypeError) as e:
            Rectangle('10', 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")
        
        #test height type and value
        with self.assertRaises(TypeError) as e:
            Rectangle(10, [2])
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -1)
        self.assertEqual(str(e.exception), "height must be > 0")

        #test x
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, (2,))
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

        #test y
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 2, (2,))
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    @unittest.mock.patch('builtins.print')
    def test_display(self, mock_print):
        r1 = Rectangle(3, 2, 2, 2)
        r1.display()
        mock_print.assert_called_with('\n\n  ###\n  ###\n', end='')
