import unittest

from textutil import count_spaces


class CountSpacesTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_spaces(""), 0)

    def test_no_spaces(self):
        self.assertEqual(count_spaces("abc"), 0)
        self.assertEqual(count_spaces("HelloWorld"), 0)
        self.assertEqual(count_spaces("123"), 0)

    def test_several_spaces(self):
        self.assertEqual(count_spaces("Hello World"), 1)
        self.assertEqual(count_spaces("a b c"), 2)
        self.assertEqual(count_spaces("  "), 2)
        self.assertEqual(count_spaces("Hello  World  Test"), 4)
        self.assertEqual(count_spaces(" leading and trailing "), 4)


if __name__ == "__main__":
    unittest.main()
