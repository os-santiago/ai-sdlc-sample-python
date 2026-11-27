import unittest

from mathutil import mean_int


class MeanIntTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(mean_int([]), 0)

    def test_one_value(self):
        self.assertEqual(mean_int([5]), 5)

    def test_non_integer_mean(self):
        self.assertEqual(mean_int([1, 2]), 1)  # mean is 1.5, floor is 1
        self.assertEqual(mean_int([1, 2, 3, 4]), 2)  # mean is 2.5, floor is 2


if __name__ == "__main__":
    unittest.main()
