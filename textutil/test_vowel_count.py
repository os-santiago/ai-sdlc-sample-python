import unittest

from textutil import vowel_count


class VowelCountTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(vowel_count(""), 0)

    def test_mixed_case(self):
        self.assertEqual(vowel_count("Hello World"), 3)
        self.assertEqual(vowel_count("AEIOUaeiou"), 10)
        self.assertEqual(vowel_count("Programming"), 3)

    def test_no_vowels(self):
        self.assertEqual(vowel_count("bcdfg"), 0)
        self.assertEqual(vowel_count("XYZ"), 0)
        self.assertEqual(vowel_count("123"), 0)


if __name__ == "__main__":
    unittest.main()
