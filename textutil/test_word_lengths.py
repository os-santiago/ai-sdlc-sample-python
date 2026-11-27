import unittest

from textutil import word_lengths


class WordLengthsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(word_lengths(""), [])
        self.assertEqual(word_lengths("   "), [])

    def test_one_word(self):
        self.assertEqual(word_lengths("hello"), [5])
        self.assertEqual(word_lengths("  hi  "), [2])

    def test_several_words(self):
        self.assertEqual(word_lengths("one two three"), [3, 3, 5])

    def test_extra_spaces(self):
        self.assertEqual(word_lengths("  one  two  three  "), [3, 3, 5])
        self.assertEqual(word_lengths("a\tb\nc"), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()
