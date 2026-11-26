import unittest

from textutil import to_snake_case


class ToSnakeCaseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(to_snake_case(""), "")

    def test_several_words(self):
        self.assertEqual(to_snake_case("hello big world"), "hello_big_world")

    def test_extra_spaces(self):
        self.assertEqual(to_snake_case("  Hello   World  "), "hello_world")

    def test_mixed_case(self):
        self.assertEqual(to_snake_case("CamelCase Example"), "camelcase_example")


if __name__ == "__main__":
    unittest.main()
