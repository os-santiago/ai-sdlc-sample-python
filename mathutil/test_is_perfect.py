import unittest

from mathutil import is_perfect


class IsPerfectTest(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_perfect(0))

    def test_one(self):
        self.assertFalse(is_perfect(1))

    def test_six(self):
        self.assertTrue(is_perfect(6))

    def test_twenty_eight(self):
        self.assertTrue(is_perfect(28))

    def test_twelve(self):
        self.assertFalse(is_perfect(12))


if __name__ == "__main__":
    unittest.main()
