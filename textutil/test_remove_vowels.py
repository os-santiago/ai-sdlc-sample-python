import unittest

from textutil import remove_vowels


class RemoveVowelsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(remove_vowels(""), "")

    def test_mixed_case(self):
        self.assertEqual(remove_vowels("Hello World"), "Hll Wrld")

    def test_no_vowels(self):
        self.assertEqual(remove_vowels("xyz"), "xyz")


if __name__ == "__main__":
    unittest.main()
