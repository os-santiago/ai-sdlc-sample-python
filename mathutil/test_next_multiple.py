import unittest

from mathutil.next_multiple import next_multiple


class NextMultipleTest(unittest.TestCase):
    def test_step_zero(self):
        # When step is 0, return n unchanged
        self.assertEqual(next_multiple(10, 0), 10)
        self.assertEqual(next_multiple(0, 0), 0)
        self.assertEqual(next_multiple(-5, 0), -5)

    def test_negative_step(self):
        # When step is negative, return n unchanged
        self.assertEqual(next_multiple(10, -3), 10)
        self.assertEqual(next_multiple(-5, -2), -5)

    def test_exact_multiple(self):
        # When n is already a multiple of step
        self.assertEqual(next_multiple(10, 5), 10)
        self.assertEqual(next_multiple(0, 3), 0)
        self.assertEqual(next_multiple(21, 7), 21)

    def test_between_multiples(self):
        # When n is between multiples
        self.assertEqual(next_multiple(7, 3), 9)
        self.assertEqual(next_multiple(23, 10), 30)
        self.assertEqual(next_multiple(14, 5), 15)

    def test_negative_n(self):
        # Test with negative n
        self.assertEqual(next_multiple(-7, 3), -6)
        self.assertEqual(next_multiple(-10, 5), -10)
        self.assertEqual(next_multiple(-11, 5), -10)


if __name__ == "__main__":
    unittest.main()
