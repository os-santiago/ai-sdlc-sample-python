import unittest

from kv import count_empty_values


class CountEmptyValuesTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(count_empty_values({}), 0)

    def test_no_empty_values(self):
        self.assertEqual(count_empty_values({"a": "1", "b": "2", "c": "3"}), 0)

    def test_all_empty_values(self):
        self.assertEqual(count_empty_values({"a": "", "b": "", "c": ""}), 3)

    def test_some_empty_values(self):
        self.assertEqual(count_empty_values({"a": "x", "b": "", "c": "y", "d": ""}), 2)


if __name__ == "__main__":
    unittest.main()
