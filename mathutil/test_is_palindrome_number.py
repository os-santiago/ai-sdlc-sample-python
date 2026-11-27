import unittest

from mathutil import is_palindrome_number


class IsPalindromeNumberTest(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_palindrome_number(0))

    def test_palindrome_121(self):
        self.assertTrue(is_palindrome_number(121))

    def test_non_palindrome_123(self):
        self.assertFalse(is_palindrome_number(123))

    def test_negative_121(self):
        self.assertFalse(is_palindrome_number(-121))


if __name__ == "__main__":
    unittest.main()
