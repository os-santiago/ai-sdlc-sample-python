import unittest

from kv import longest_key


class LongestKeyTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertIsNone(longest_key({}))

    def test_tie(self):
        # Multiple keys with same length: should return the smallest
        self.assertEqual(longest_key({"abc": "1", "xyz": "2", "def": "3"}), "abc")
        self.assertEqual(longest_key({"zz": "1", "aa": "2", "mm": "3"}), "aa")

    def test_distinct_lengths(self):
        # Keys with different lengths: should return the longest
        self.assertEqual(longest_key({"a": "1", "abc": "2", "ab": "3"}), "abc")
        self.assertEqual(longest_key({"short": "1", "verylongkey": "2", "mid": "3"}), "verylongkey")
        self.assertEqual(longest_key({"x": "1", "xyz": "2"}), "xyz")


if __name__ == "__main__":
    unittest.main()
