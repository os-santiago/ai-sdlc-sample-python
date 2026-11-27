import unittest

from textutil import first_char


class FirstCharTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(first_char(""), "")

    def test_leading_spaces(self):
        self.assertEqual(first_char("   hello"), "h")

    def test_normal_word(self):
        self.assertEqual(first_char("word"), "w")

    def test_all_whitespace(self):
        self.assertEqual(first_char("   \t\n  "), "")


if __name__ == "__main__":
    unittest.main()
