import unittest

from mathutil import count_divisors


class CountDivisorsTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_divisors(0), 0)

    def test_negative(self):
        self.assertEqual(count_divisors(-5), 0)
        self.assertEqual(count_divisors(-1), 0)

    def test_one(self):
        self.assertEqual(count_divisors(1), 1)

    def test_prime(self):
        self.assertEqual(count_divisors(7), 2)
        self.assertEqual(count_divisors(13), 2)

    def test_twelve(self):
        # 12 has divisors: 1, 2, 3, 4, 6, 12
        self.assertEqual(count_divisors(12), 6)

    def test_additional_cases(self):
        self.assertEqual(count_divisors(2), 2)  # prime
        self.assertEqual(count_divisors(4), 3)  # 1, 2, 4
        self.assertEqual(count_divisors(16), 5)  # 1, 2, 4, 8, 16
        self.assertEqual(count_divisors(100), 9)  # 1, 2, 4, 5, 10, 20, 25, 50, 100


if __name__ == "__main__":
    unittest.main()
