"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Testing adding numbers together."""
        res = calc.add(5,6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        """Testing subracting numbers."""
        res = calc.subtract(10,15)

        self.assertEquals(res, 5)

    def test_multiply_numbers(self):
        """Testing multiplying numbers."""
        res = calc.multiply(3,3)

        self.assertEquals(res,9)
