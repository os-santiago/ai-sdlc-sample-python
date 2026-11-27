import unittest

from textutil import alternate_case


class AlternateCaseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(alternate_case(""), "")

    def test_one_character(self):
        self.assertEqual(alternate_case("a"), "A")

    def test_mixed_word(self):
        self.assertEqual(alternate_case("hello"), "HeLlO")


if __name__ == "__main__":
    unittest.main()
