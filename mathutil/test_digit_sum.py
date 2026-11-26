import unittest

from mathutil import digit_sum


class DigitSumTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(digit_sum(0), 0)

    def test_positive(self):
        self.assertEqual(digit_sum(123), 6)
        self.assertEqual(digit_sum(999), 27)

    def test_negative(self):
        self.assertEqual(digit_sum(-123), 6)
        self.assertEqual(digit_sum(-456), 15)


if __name__ == "__main__":
    unittest.main()
