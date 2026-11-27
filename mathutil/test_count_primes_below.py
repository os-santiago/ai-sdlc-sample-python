import unittest

from mathutil import count_primes_below


class CountPrimesBelowTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_primes_below(0), 0)

    def test_two(self):
        self.assertEqual(count_primes_below(2), 0)

    def test_ten(self):
        # Primes: 2, 3, 5, 7
        self.assertEqual(count_primes_below(10), 4)

    def test_thirty(self):
        # Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        self.assertEqual(count_primes_below(30), 10)


if __name__ == "__main__":
    unittest.main()
