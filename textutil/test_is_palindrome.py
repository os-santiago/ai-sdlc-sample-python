import unittest

from textutil import is_palindrome


class IsPalindromeTest(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_simple(self):
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("levels"))

    def test_case_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    unittest.main()
