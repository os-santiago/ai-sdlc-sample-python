import unittest

from kv import omit


class OmitTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(omit(None, ["a"]), {})

    def test_remove_some_keys(self):
        self.assertEqual(omit({"a": "1", "b": "2", "c": "3"}, ["a", "c"]), {"b": "2"})

    def test_missing_keys(self):
        self.assertEqual(omit({"a": "1", "b": "2"}, ["x", "a"]), {"b": "2"})

    def test_input_not_modified(self):
        original = {"a": "1", "b": "2", "c": "3"}
        result = omit(original, ["a"])
        self.assertEqual(original, {"a": "1", "b": "2", "c": "3"})
        self.assertEqual(result, {"b": "2", "c": "3"})


if __name__ == "__main__":
    unittest.main()
