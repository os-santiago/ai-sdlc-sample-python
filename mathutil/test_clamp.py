import unittest

from mathutil import clamp


class ClampTest(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_bounds(self):
        self.assertEqual(clamp(-3, 0, 10), 0)
        self.assertEqual(clamp(42, 0, 10), 10)
        self.assertEqual(clamp(0, 0, 0), 0)

    def test_inverted_range(self):
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)


if __name__ == "__main__":
    unittest.main()
