import unittest

from textutil import count_uppercase


class CountUppercaseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_uppercase(""), 0)

    def test_mixed_case(self):
        self.assertEqual(count_uppercase("Hello World"), 2)
        self.assertEqual(count_uppercase("HELLO"), 5)
        self.assertEqual(count_uppercase("hello"), 0)
        self.assertEqual(count_uppercase("AbCdEf"), 3)

    def test_digits(self):
        self.assertEqual(count_uppercase("123"), 0)
        self.assertEqual(count_uppercase("ABC123"), 3)
        self.assertEqual(count_uppercase("123ABC456"), 3)
        self.assertEqual(count_uppercase("A1B2C3"), 3)


if __name__ == "__main__":
    unittest.main()
