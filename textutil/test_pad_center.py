import unittest

from textutil import pad_center


class PadCenterTest(unittest.TestCase):
    def test_width_below_length(self):
        # Width less than string length - return unchanged
        self.assertEqual(pad_center("hello", 3), "hello")
        self.assertEqual(pad_center("test", 2), "test")
        
    def test_width_equal_length(self):
        # Width equal to string length - return unchanged
        self.assertEqual(pad_center("hi", 2), "hi")
        
    def test_even_split(self):
        # Even padding - equal on both sides
        self.assertEqual(pad_center("hi", 6), "  hi  ")
        self.assertEqual(pad_center("x", 5, "*"), "**x**")
        
    def test_odd_split(self):
        # Odd padding - extra goes on the right
        self.assertEqual(pad_center("hi", 7), "  hi   ")
        self.assertEqual(pad_center("x", 4, "-"), "-x--")
        
    def test_custom_fill(self):
        self.assertEqual(pad_center("test", 10, "*"), "***test***")


if __name__ == "__main__":
    unittest.main()
