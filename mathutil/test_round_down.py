import unittest

from mathutil.round_down import round_down


class RoundDownTest(unittest.TestCase):
    def test_step_zero(self):
        # When step is 0, return n unchanged
        self.assertEqual(round_down(10, 0), 10)
        self.assertEqual(round_down(0, 0), 0)
        self.assertEqual(round_down(-5, 0), -5)

    def test_negative_step(self):
        # When step is negative, return n unchanged
        self.assertEqual(round_down(10, -3), 10)
        self.assertEqual(round_down(-5, -2), -5)

    def test_negative_n(self):
        # Test with negative n
        self.assertEqual(round_down(-7, 3), -9)
        self.assertEqual(round_down(-10, 5), -10)

    def test_exact_multiple(self):
        # When n is already a multiple of step
        self.assertEqual(round_down(10, 5), 10)
        self.assertEqual(round_down(0, 3), 0)
        self.assertEqual(round_down(21, 7), 21)

    def test_between_multiples(self):
        # When n is between multiples
        self.assertEqual(round_down(7, 3), 6)
        self.assertEqual(round_down(23, 10), 20)
        self.assertEqual(round_down(14, 5), 10)


if __name__ == "__main__":
    unittest.main()
