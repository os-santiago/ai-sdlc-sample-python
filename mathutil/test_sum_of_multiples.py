import unittest

from mathutil.sum_of_multiples import sum_of_multiples


class SumOfMultiplesTest(unittest.TestCase):
    def test_k_zero(self):
        self.assertEqual(sum_of_multiples(10, 0), 0)

    def test_n_ten_k_three(self):
        # Multiples of 3 less than 10: 3, 6, 9
        # Sum: 3 + 6 + 9 = 18
        self.assertEqual(sum_of_multiples(10, 3), 18)

    def test_n_one(self):
        # No positive multiples less than 1
        self.assertEqual(sum_of_multiples(1, 3), 0)

    def test_k_negative(self):
        self.assertEqual(sum_of_multiples(10, -1), 0)

    def test_n_zero(self):
        self.assertEqual(sum_of_multiples(0, 3), 0)

    def test_n_negative(self):
        self.assertEqual(sum_of_multiples(-5, 3), 0)

    def test_multiples_of_five_below_twenty(self):
        # Multiples of 5 less than 20: 5, 10, 15
        # Sum: 5 + 10 + 15 = 30
        self.assertEqual(sum_of_multiples(20, 5), 30)

    def test_multiples_of_seven_below_thirty(self):
        # Multiples of 7 less than 30: 7, 14, 21, 28
        # Sum: 7 + 14 + 21 + 28 = 70
        self.assertEqual(sum_of_multiples(30, 7), 70)


if __name__ == "__main__":
    unittest.main()
