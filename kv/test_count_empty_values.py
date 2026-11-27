import unittest

from kv.count_empty_values import count_empty_values


class CountEmptyValuesTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(count_empty_values({}), 0)

    def test_no_empty_values(self):
        self.assertEqual(count_empty_values({"a": "1", "b": "2", "c": "3"}), 0)

    def test_several_empty_values(self):
        self.assertEqual(count_empty_values({"a": "", "b": "x", "c": "", "d": ""}), 3)

    def test_all_empty_values(self):
        self.assertEqual(count_empty_values({"a": "", "b": ""}), 2)

    def test_single_empty_value(self):
        self.assertEqual(count_empty_values({"a": "x", "b": ""}), 1)


if __name__ == "__main__":
    unittest.main()
