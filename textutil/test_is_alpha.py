import unittest

from textutil import is_alpha


class IsAlphaTest(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(is_alpha(""))

    def test_letters_only(self):
        self.assertTrue(is_alpha("abc"))
        self.assertTrue(is_alpha("ABC"))
        self.assertTrue(is_alpha("AbCdEf"))

    def test_accented_letters(self):
        self.assertTrue(is_alpha("café"))
        self.assertTrue(is_alpha("naïve"))
        self.assertTrue(is_alpha("résumé"))

    def test_with_digit(self):
        self.assertFalse(is_alpha("abc1"))
        self.assertFalse(is_alpha("1abc"))
        self.assertFalse(is_alpha("a1b"))

    def test_with_space(self):
        self.assertFalse(is_alpha("hello world"))
        self.assertFalse(is_alpha(" abc"))
        self.assertFalse(is_alpha("abc "))


if __name__ == "__main__":
    unittest.main()
