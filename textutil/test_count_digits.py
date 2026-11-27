import unittest

from textutil import count_digits


class CountDigitsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_digits(""), 0)

    def test_no_digits(self):
        self.assertEqual(count_digits("abc"), 0)
        self.assertEqual(count_digits("Hello World"), 0)
        self.assertEqual(count_digits("ABC xyz"), 0)

    def test_mixed_text(self):
        self.assertEqual(count_digits("123"), 3)
        self.assertEqual(count_digits("a1b2c3"), 3)
        self.assertEqual(count_digits("Hello 123 World"), 3)
        self.assertEqual(count_digits("Test 1 and 2 and 3"), 3)
        self.assertEqual(count_digits("2024-01-15"), 8)


if __name__ == "__main__":
    unittest.main()
