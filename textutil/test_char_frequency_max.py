import unittest

from textutil import char_frequency_max


class CharFrequencyMaxTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(char_frequency_max(""), "")

    def test_tie(self):
        self.assertEqual(char_frequency_max("aabbcc"), "a")

    def test_clear_winner(self):
        self.assertEqual(char_frequency_max("aabbbcc"), "b")


if __name__ == "__main__":
    unittest.main()
