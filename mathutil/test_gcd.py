import unittest

from mathutil import gcd


class GcdTest(unittest.TestCase):
    def test_common(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(7, 13), 1)

    def test_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_negative(self):
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(-12, -18), 6)


if __name__ == "__main__":
    unittest.main()
