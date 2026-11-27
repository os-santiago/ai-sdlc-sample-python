import unittest

from kv import upper_keys


class UpperKeysTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(upper_keys({}), {})

    def test_distinct_keys(self):
        self.assertEqual(upper_keys({"a": "1", "b": "2"}), {"A": "1", "B": "2"})

    def test_collision(self):
        # "a" > "A" lexically, so "a"'s value wins
        self.assertEqual(upper_keys({"a": "lower", "A": "upper"}), {"A": "lower"})


if __name__ == "__main__":
    unittest.main()
