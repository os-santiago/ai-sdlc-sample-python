import unittest

from textutil import is_title_case


class IsTitleCaseTest(unittest.TestCase):
    def test_empty(self):
        self.assertFalse(is_title_case(""))

    def test_title_case_phrase(self):
        self.assertTrue(is_title_case("Hello World"))
        self.assertTrue(is_title_case("The Quick Brown Fox"))

    def test_phrase_with_lowercase_word(self):
        self.assertFalse(is_title_case("hello world"))
        self.assertFalse(is_title_case("Hello world"))
        self.assertFalse(is_title_case("hello World"))


if __name__ == "__main__":
    unittest.main()
