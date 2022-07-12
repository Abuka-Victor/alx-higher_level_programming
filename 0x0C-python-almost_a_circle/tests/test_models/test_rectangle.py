""" Test Module for rectangle.py """
import unittest
Rectangle = __import__("models.rectangle").rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for rectangle.py """

    def test_id(self):
        self.assertEqual(Rectangle(10, 12).id, 1)
