import unittest

from mathutil import collatz_steps


class CollatzStepsTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(collatz_steps(1), 0)

    def test_zero(self):
        self.assertEqual(collatz_steps(0), 0)

    def test_six(self):
        self.assertEqual(collatz_steps(6), 8)

    def test_seven(self):
        self.assertEqual(collatz_steps(7), 16)


if __name__ == "__main__":
    unittest.main()
