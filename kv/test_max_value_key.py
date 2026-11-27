import unittest

from kv import max_value_key


class MaxValueKeyTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertIsNone(max_value_key({}))

    def test_tie(self):
        # Multiple keys with same max value - should return smallest key
        self.assertEqual(max_value_key({"a": 5, "b": 5, "c": 3}), "a")
        self.assertEqual(max_value_key({"z": 10, "a": 10, "m": 5}), "a")

    def test_distinct_values(self):
        self.assertEqual(max_value_key({"x": 1, "y": 10, "z": 5}), "y")
        self.assertEqual(max_value_key({"a": 100, "b": 50, "c": 75}), "a")
        self.assertEqual(max_value_key({"low": -5, "high": 42, "mid": 0}), "high")


if __name__ == "__main__":
    unittest.main()
