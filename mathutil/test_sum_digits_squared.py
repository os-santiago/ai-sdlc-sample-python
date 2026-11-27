import unittest

from mathutil import sum_digits_squared


class SumDigitsSquaredTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_digits_squared(0), 0)

    def test_single_digit(self):
        self.assertEqual(sum_digits_squared(5), 25)
        self.assertEqual(sum_digits_squared(9), 81)

    def test_negative(self):
        self.assertEqual(sum_digits_squared(-5), 25)
        self.assertEqual(sum_digits_squared(-123), 14)

    def test_123(self):
        # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
        self.assertEqual(sum_digits_squared(123), 14)


if __name__ == "__main__":
    unittest.main()
