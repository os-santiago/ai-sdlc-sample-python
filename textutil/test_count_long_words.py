import unittest

from textutil import count_long_words


class CountLongWordsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_long_words("", 3), 0)
        self.assertEqual(count_long_words("   ", 5), 0)

    def test_n_zero(self):
        self.assertEqual(count_long_words("hello world", 0), 2)
        self.assertEqual(count_long_words("a b c", 0), 3)

    def test_excludes_short_words(self):
        self.assertEqual(count_long_words("I am a developer", 3), 1)
        self.assertEqual(count_long_words("the quick brown fox", 4), 2)
        self.assertEqual(count_long_words("a bb ccc dddd", 3), 2)


if __name__ == "__main__":
    unittest.main()
