import unittest

from mathutil import is_odd


class IsOddTest(unittest.TestCase):
    def test_values(self):
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(-3))
        self.assertFalse(is_odd(4))

    def test_negative_odd(self):
        self.assertTrue(is_odd(-1))
        self.assertTrue(is_odd(-5))

    def test_positive_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(7))


if __name__ == "__main__":
    unittest.main()
