import unittest

from mathutil import is_square_sum


class IsSquareSumTest(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(is_square_sum(-1))

    def test_zero(self):
        self.assertTrue(is_square_sum(0))

    def test_five(self):
        self.assertTrue(is_square_sum(5))

    def test_three(self):
        self.assertFalse(is_square_sum(3))

    def test_twenty_five(self):
        self.assertTrue(is_square_sum(25))


if __name__ == "__main__":
    unittest.main()
