import unittest

from textutil import last_word


class LastWordTest(unittest.TestCase):
    def test_blank_input(self):
        self.assertEqual(last_word(""), "")

    def test_all_whitespace(self):
        self.assertEqual(last_word("   "), "")

    def test_one_word(self):
        self.assertEqual(last_word("hello"), "hello")

    def test_trailing_spaces(self):
        self.assertEqual(last_word("hello  "), "hello")

    def test_multiple_words(self):
        self.assertEqual(last_word("hello world"), "world")

    def test_multiple_words_with_trailing_spaces(self):
        self.assertEqual(last_word("hello world  "), "world")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(last_word("  hello world  "), "world")


if __name__ == "__main__":
    unittest.main()
