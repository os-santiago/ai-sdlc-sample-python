import unittest

from mathutil.lcm import lcm


class LcmTest(unittest.TestCase):
    def test_coprime(self):
        # Test coprime values (gcd = 1)
        self.assertEqual(lcm(7, 13), 91)
        self.assertEqual(lcm(5, 9), 45)

    def test_shared_factor(self):
        # Test values with a shared factor
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(6, 15), 30)

    def test_zero(self):
        # Test zero inputs
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_negative(self):
        # Test negative inputs - should return non-negative result
        self.assertEqual(lcm(-12, 18), 36)
        self.assertEqual(lcm(12, -18), 36)
        self.assertEqual(lcm(-12, -18), 36)


if __name__ == "__main__":
    unittest.main()
