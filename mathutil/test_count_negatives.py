import unittest

from mathutil.count_negatives import count_negatives


class CountNegativesTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_negatives([]), 0)

    def test_no_negatives(self):
        # Only zero and positive values
        self.assertEqual(count_negatives([0, 1, 2, 3]), 0)

    def test_mix(self):
        # -3, -1 are negative (count=2); 0, 2, 5 are not negative
        self.assertEqual(count_negatives([-3, -1, 0, 2, 5]), 2)

    def test_all_negatives(self):
        # All three values are negative
        self.assertEqual(count_negatives([-5, -2, -1]), 3)

    def test_single_negative(self):
        self.assertEqual(count_negatives([-1]), 1)

    def test_zero_boundary(self):
        # Only -1 is negative; 0 and 1 are not negative
        self.assertEqual(count_negatives([-1, 0, 1]), 1)

    def test_multiple_same_negative(self):
        # Three instances of -5
        self.assertEqual(count_negatives([-5, -5, -5]), 3)

    def test_mixed_with_duplicates(self):
        # Negatives: -2, -2, -1 (count=3)
        self.assertEqual(count_negatives([5, -2, 0, -2, -1, 10]), 3)


if __name__ == "__main__":
    unittest.main()
