import unittest

from mathutil import sum_range


class SumRangeTest(unittest.TestCase):
    def test_range(self):
        self.assertEqual(sum_range(1, 10), 55)
        self.assertEqual(sum_range(-3, 3), 0)

    def test_single(self):
        self.assertEqual(sum_range(4, 4), 4)

    def test_empty(self):
        self.assertEqual(sum_range(5, 1), 0)


if __name__ == "__main__":
    unittest.main()
