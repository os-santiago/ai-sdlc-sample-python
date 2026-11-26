import unittest

from textutil import longest_word


class LongestWordTest(unittest.TestCase):
    def test_blank_input(self):
        # Empty string
        self.assertEqual(longest_word(""), "")
        # Whitespace only
        self.assertEqual(longest_word("   "), "")
        self.assertEqual(longest_word("\t\n  "), "")

    def test_tie_first_wins(self):
        # All words have the same length - first should win
        self.assertEqual(longest_word("cat dog bat"), "cat")
        self.assertEqual(longest_word("aa bb cc"), "aa")

    def test_several_words(self):
        # Clear winner
        self.assertEqual(longest_word("a bb ccc dddd"), "dddd")
        self.assertEqual(longest_word("short medium verylongword"), "verylongword")
        # Longest word in the middle
        self.assertEqual(longest_word("hi hello yo"), "hello")
        # Longest word at the beginning
        self.assertEqual(longest_word("wonderful hi yo"), "wonderful")

    def test_single_word(self):
        self.assertEqual(longest_word("hello"), "hello")

    def test_extra_whitespace(self):
        self.assertEqual(longest_word("  one\ttwo\n three  "), "three")


if __name__ == "__main__":
    unittest.main()
