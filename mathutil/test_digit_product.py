import unittest

from mathutil import digit_product


class DigitProductTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(digit_product(0), 0)

    def test_single_digit(self):
        self.assertEqual(digit_product(7), 7)

    def test_negative(self):
        self.assertEqual(digit_product(-5), 5)

    def test_234(self):
        self.assertEqual(digit_product(234), 24)


if __name__ == "__main__":
    unittest.main()
