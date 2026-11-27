import unittest

from textutil import capitalize_first


class CapitalizeFirstTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(capitalize_first(""), "")

    def test_lowercase_word(self):
        self.assertEqual(capitalize_first("hello"), "Hello")

    def test_already_capitalized(self):
        self.assertEqual(capitalize_first("World"), "World")


if __name__ == "__main__":
    unittest.main()
