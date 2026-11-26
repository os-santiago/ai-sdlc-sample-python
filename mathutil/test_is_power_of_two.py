import unittest

from mathutil import is_power_of_two


class IsPowerOfTwoTest(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_power_of_two(0))

    def test_negative(self):
        self.assertFalse(is_power_of_two(-8))

    def test_one(self):
        self.assertTrue(is_power_of_two(1))

    def test_powers_of_two(self):
        self.assertTrue(is_power_of_two(64))

    def test_non_power_of_two(self):
        self.assertFalse(is_power_of_two(12))


if __name__ == "__main__":
    unittest.main()
