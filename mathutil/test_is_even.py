import unittest

from mathutil import is_even


class IsEvenTest(unittest.TestCase):
    def test_values(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_negative(self):
        self.assertTrue(is_even(-2))
        self.assertFalse(is_even(-3))


if __name__ == "__main__":
    unittest.main()
