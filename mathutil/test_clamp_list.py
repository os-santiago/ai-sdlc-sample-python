import unittest

from mathutil import clamp_list


class ClampListTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(clamp_list([], 0, 10), [])

    def test_values_inside(self):
        self.assertEqual(clamp_list([3, 5, 7], 0, 10), [3, 5, 7])

    def test_values_below(self):
        self.assertEqual(clamp_list([-5, -2, -10], 0, 10), [0, 0, 0])

    def test_values_above(self):
        self.assertEqual(clamp_list([15, 20, 100], 0, 10), [10, 10, 10])

    def test_mixed_values(self):
        self.assertEqual(clamp_list([-5, 3, 7, 15], 0, 10), [0, 3, 7, 10])

    def test_at_boundaries(self):
        self.assertEqual(clamp_list([0, 5, 10], 0, 10), [0, 5, 10])

    def test_inverted_range(self):
        with self.assertRaises(ValueError):
            clamp_list([1, 2, 3], 10, 0)


if __name__ == "__main__":
    unittest.main()
