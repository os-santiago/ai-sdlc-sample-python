import unittest

from textutil import strip_punctuation


class StripPunctuationTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(strip_punctuation(""), "")

    def test_sentence_with_punctuation(self):
        self.assertEqual(strip_punctuation("Hello, World!"), "Hello World")

    def test_text_without_punctuation(self):
        self.assertEqual(strip_punctuation("HelloWorld"), "HelloWorld")


if __name__ == "__main__":
    unittest.main()
