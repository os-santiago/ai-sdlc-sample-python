import unittest

from mathutil import is_triangular


class IsTriangularTest(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_triangular(0))

    def test_one(self):
        self.assertTrue(is_triangular(1))

    def test_three(self):
        self.assertTrue(is_triangular(3))

    def test_ten(self):
        self.assertTrue(is_triangular(10))

    def test_eleven(self):
        self.assertFalse(is_triangular(11))

    def test_additional_triangular(self):
        # Additional triangular numbers: 6, 15, 21
        self.assertTrue(is_triangular(6))   # k=3: 3*4/2=6
        self.assertTrue(is_triangular(15))  # k=5: 5*6/2=15
        self.assertTrue(is_triangular(21))  # k=6: 6*7/2=21

    def test_non_triangular(self):
        self.assertFalse(is_triangular(2))
        self.assertFalse(is_triangular(5))
        self.assertFalse(is_triangular(100))

    def test_negative(self):
        self.assertFalse(is_triangular(-1))
        self.assertFalse(is_triangular(-10))


if __name__ == "__main__":
    unittest.main()
