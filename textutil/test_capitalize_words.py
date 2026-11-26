import unittest

from textutil import capitalize_words


class CapitalizeWordsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(capitalize_words(""), "")

    def test_words(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")

    def test_keeps_rest_and_collapses_spaces(self):
        self.assertEqual(capitalize_words("  mcDonald   iPhone "), "McDonald IPhone")


if __name__ == "__main__":
    unittest.main()
