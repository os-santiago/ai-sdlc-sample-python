import unittest

from textutil import initials


class InitialsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(initials(""), "")

    def test_one_word(self):
        self.assertEqual(initials("hello"), "H")

    def test_several_words(self):
        self.assertEqual(initials("hello big world"), "HBW")

    def test_extra_spaces(self):
        self.assertEqual(initials("  hello   big  world  "), "HBW")

    def test_mixed_case_input(self):
        self.assertEqual(initials("john paul jones"), "JPJ")


if __name__ == "__main__":
    unittest.main()
