import unittest

from textutil import count_words_with


class CountWordsWithTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_words_with("", "a"), 0)
        self.assertEqual(count_words_with("   ", "x"), 0)

    def test_no_match(self):
        self.assertEqual(count_words_with("hello world", "z"), 0)
        self.assertEqual(count_words_with("the quick brown fox", "z"), 0)

    def test_several_matches(self):
        self.assertEqual(count_words_with("the cat sat on the mat", "a"), 3)
        self.assertEqual(count_words_with("apple orange banana", "a"), 3)
        self.assertEqual(count_words_with("one two three four", "o"), 3)

    def test_case_sensitive(self):
        self.assertEqual(count_words_with("Apple apple", "A"), 1)
        self.assertEqual(count_words_with("Apple apple", "a"), 1)

    def test_single_word(self):
        self.assertEqual(count_words_with("banana", "a"), 1)
        self.assertEqual(count_words_with("hello", "z"), 0)


if __name__ == "__main__":
    unittest.main()
