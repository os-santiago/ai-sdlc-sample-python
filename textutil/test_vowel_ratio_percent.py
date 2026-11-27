import unittest

from textutil import vowel_ratio_percent


class VowelRatioPercentTest(unittest.TestCase):
    def test_no_letters(self):
        self.assertEqual(vowel_ratio_percent(""), 0)
        self.assertEqual(vowel_ratio_percent("123"), 0)
        self.assertEqual(vowel_ratio_percent("!@#$%"), 0)

    def test_all_vowels(self):
        self.assertEqual(vowel_ratio_percent("aeiou"), 100)
        self.assertEqual(vowel_ratio_percent("AEIOU"), 100)
        self.assertEqual(vowel_ratio_percent("aEiOu"), 100)

    def test_mixed_word(self):
        self.assertEqual(vowel_ratio_percent("hello"), 40)
        self.assertEqual(vowel_ratio_percent("world"), 20)
        self.assertEqual(vowel_ratio_percent("rhythm"), 0)


if __name__ == "__main__":
    unittest.main()
