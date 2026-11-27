import unittest

from kv import min_value_key


class MinValueKeyTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertIsNone(min_value_key({}))

    def test_tie(self):
        # Multiple keys with same min value - should return smallest key
        self.assertEqual(min_value_key({"a": 5, "b": 5, "c": 10}), "a")
        self.assertEqual(min_value_key({"z": 3, "a": 3, "m": 5}), "a")

    def test_distinct_values(self):
        self.assertEqual(min_value_key({"x": 10, "y": 1, "z": 5}), "y")
        self.assertEqual(min_value_key({"a": 100, "b": 50, "c": 75}), "b")
        self.assertEqual(min_value_key({"low": -5, "high": 42, "mid": 0}), "low")


if __name__ == "__main__":
    unittest.main()
