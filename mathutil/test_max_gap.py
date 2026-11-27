import unittest

from mathutil import max_gap


class MaxGapTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_gap([]), 0)

    def test_one_value(self):
        self.assertEqual(max_gap([5]), 0)

    def test_unsorted_list(self):
        # [3, 1, 5, 2] -> sorted: [1, 2, 3, 5]
        # gaps: 1, 1, 2 -> max: 2
        self.assertEqual(max_gap([3, 1, 5, 2]), 2)

    def test_two_values(self):
        self.assertEqual(max_gap([1, 5]), 4)

    def test_all_same(self):
        self.assertEqual(max_gap([3, 3, 3]), 0)

    def test_negative_values(self):
        # [-5, 2, -1, 8] -> sorted: [-5, -1, 2, 8]
        # gaps: 4, 3, 6 -> max: 6
        self.assertEqual(max_gap([-5, 2, -1, 8]), 6)


if __name__ == "__main__":
    unittest.main()
