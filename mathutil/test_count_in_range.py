import unittest

from mathutil.count_in_range import count_in_range


class CountInRangeTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_in_range([], 0, 10), 0)

    def test_inverted_range(self):
        self.assertEqual(count_in_range([1, 2, 3], 10, 0), 0)

    def test_mixed_values(self):
        # Values: -5 (outside), 0 (inside), 5 (inside), 10 (inside), 15 (outside)
        self.assertEqual(count_in_range([-5, 0, 5, 10, 15], 0, 10), 3)

    def test_all_inside(self):
        self.assertEqual(count_in_range([1, 2, 3, 4, 5], 0, 10), 5)

    def test_all_outside(self):
        self.assertEqual(count_in_range([11, 12, 13], 0, 10), 0)

    def test_boundary_values(self):
        # Test that boundaries are inclusive
        self.assertEqual(count_in_range([0, 5, 10], 0, 10), 3)
        self.assertEqual(count_in_range([-1, 0, 10, 11], 0, 10), 2)

    def test_single_value_range(self):
        self.assertEqual(count_in_range([5, 5, 5, 3, 7], 5, 5), 3)


if __name__ == "__main__":
    unittest.main()
