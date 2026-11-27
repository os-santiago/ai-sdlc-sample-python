import unittest

from textutil import repeat_words


class RepeatWordsTest(unittest.TestCase):
    def test_n_zero(self):
        self.assertEqual(repeat_words("hello world", 0), "")
        self.assertEqual(repeat_words("one two three", 0), "")

    def test_n_negative(self):
        self.assertEqual(repeat_words("hello world", -1), "")

    def test_n_one(self):
        self.assertEqual(repeat_words("hello world", 1), "hello world")
        self.assertEqual(repeat_words("one two three", 1), "one two three")

    def test_n_two(self):
        self.assertEqual(repeat_words("hello world", 2), "hello hello world world")
        self.assertEqual(repeat_words("one two three", 2), "one one two two three three")

    def test_empty_string(self):
        self.assertEqual(repeat_words("", 2), "")

    def test_single_word(self):
        self.assertEqual(repeat_words("hello", 3), "hello hello hello")

    def test_multiple_spaces_collapsed(self):
        self.assertEqual(repeat_words("  hello   world  ", 2), "hello hello world world")


if __name__ == "__main__":
    unittest.main()
