import unittest

from textutil import count_consonants


class CountConsonantsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_consonants(""), 0)

    def test_mixed_case(self):
        self.assertEqual(count_consonants("Hello World"), 7)
        self.assertEqual(count_consonants("BCDFG"), 5)
        self.assertEqual(count_consonants("bcdfg"), 5)
        self.assertEqual(count_consonants("Programming"), 8)

    def test_non_letter_characters(self):
        self.assertEqual(count_consonants("123"), 0)
        self.assertEqual(count_consonants("!@#$%"), 0)
        self.assertEqual(count_consonants("Hello, World! 123"), 7)
        self.assertEqual(count_consonants("a1b2c3"), 2)

    def test_all_vowels(self):
        self.assertEqual(count_consonants("aeiouAEIOU"), 0)


if __name__ == "__main__":
    unittest.main()
