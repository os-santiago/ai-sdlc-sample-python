import unittest

from mathutil import abs_difference_sum


class AbsDifferenceSumTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(abs_difference_sum([]), 0)

    def test_single(self):
        self.assertEqual(abs_difference_sum([5]), 0)

    def test_ups_and_downs(self):
        # [1, 5, 2, 8]: abs(5-1) + abs(2-5) + abs(8-2) = 4 + 3 + 6 = 13
        self.assertEqual(abs_difference_sum([1, 5, 2, 8]), 13)


if __name__ == "__main__":
    unittest.main()
