import unittest

from kv import keys_sorted_by_value


class KeysSortedByValueTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(keys_sorted_by_value({}), [])

    def test_distinct_values(self):
        self.assertEqual(keys_sorted_by_value({"a": "3", "b": "1", "c": "2"}), ["b", "c", "a"])

    def test_equal_values(self):
        self.assertEqual(keys_sorted_by_value({"a": "1", "c": "1", "b": "2"}), ["a", "c", "b"])


if __name__ == "__main__":
    unittest.main()
