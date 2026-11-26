import unittest

from kv import min_key


class MinKeyTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertIsNone(min_key({}))

    def test_one_key(self):
        self.assertEqual(min_key({"a": "value"}), "a")

    def test_several_keys(self):
        self.assertEqual(min_key({"c": "3", "a": "1", "b": "2"}), "a")
        self.assertEqual(min_key({"z": "last", "m": "middle", "a": "first"}), "a")


if __name__ == "__main__":
    unittest.main()
