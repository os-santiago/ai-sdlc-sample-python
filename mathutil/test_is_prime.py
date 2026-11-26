import unittest

from mathutil import is_prime


class IsPrimeTest(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-1))

    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_small_prime(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))

    def test_composite(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))


if __name__ == "__main__":
    unittest.main()
