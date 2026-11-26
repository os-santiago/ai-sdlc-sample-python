import unittest

from textutil import word_count


class WordCountTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("   "), 0)

    def test_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_extra_whitespace(self):
        self.assertEqual(word_count("  one\ttwo\n three  "), 3)


if __name__ == "__main__":
    unittest.main()
