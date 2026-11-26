import unittest

from kv import sorted_keys


class SortedKeysTest(unittest.TestCase):
    def test_none_and_empty(self):
        self.assertEqual(sorted_keys(None), [])
        self.assertEqual(sorted_keys({}), [])

    def test_order(self):
        self.assertEqual(sorted_keys({"b": "2", "a": "1", "c": "3"}), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
