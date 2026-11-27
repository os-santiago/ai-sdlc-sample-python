import unittest

from mathutil.sum_of_evens import sum_of_evens


class SumOfEvensTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_of_evens([]), 0)

    def test_only_odd_values(self):
        self.assertEqual(sum_of_evens([1, 3, 5, 7]), 0)

    def test_mix_including_negatives(self):
        self.assertEqual(sum_of_evens([1, 2, -4, 3, 6, -1]), 4)

    def test_all_even_values(self):
        self.assertEqual(sum_of_evens([2, 4, 6]), 12)

    def test_single_even(self):
        self.assertEqual(sum_of_evens([2]), 2)

    def test_single_odd(self):
        self.assertEqual(sum_of_evens([3]), 0)

    def test_with_zero(self):
        self.assertEqual(sum_of_evens([0, 1, 2]), 2)

    def test_negative_evens(self):
        self.assertEqual(sum_of_evens([-2, -4, -6]), -12)


if __name__ == "__main__":
    unittest.main()
