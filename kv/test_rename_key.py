import unittest

from kv import rename_key


class RenameKeyTest(unittest.TestCase):
    def test_missing_key(self):
        self.assertEqual(rename_key({"a": "1", "b": "2"}, "x", "y"), {"a": "1", "b": "2"})

    def test_rename(self):
        self.assertEqual(rename_key({"a": "1", "b": "2"}, "a", "c"), {"c": "1", "b": "2"})

    def test_input_not_modified(self):
        original = {"a": "1", "b": "2"}
        result = rename_key(original, "a", "c")
        self.assertEqual(original, {"a": "1", "b": "2"})
        self.assertEqual(result, {"c": "1", "b": "2"})


if __name__ == "__main__":
    unittest.main()
