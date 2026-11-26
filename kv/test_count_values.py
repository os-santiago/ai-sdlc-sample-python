import unittest

from kv import count_values


class CountValuesTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(count_values(None), {})

    def test_empty(self):
        self.assertEqual(count_values({}), {})

    def test_unique_values(self):
        self.assertEqual(count_values({"a": "1", "b": "2", "c": "3"}), {"1": 1, "2": 1, "3": 1})

    def test_shared_value(self):
        self.assertEqual(count_values({"a": "x", "b": "x", "c": "y"}), {"x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
