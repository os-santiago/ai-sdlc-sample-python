import unittest

from kv import drop_empty


class DropEmptyTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_no_empty_values(self):
        self.assertEqual(drop_empty({"a": "1", "b": "2"}), {"a": "1", "b": "2"})

    def test_some_empty_values(self):
        self.assertEqual(drop_empty({"a": "1", "b": "", "c": "3", "d": ""}), {"a": "1", "c": "3"})

    def test_input_not_modified(self):
        original = {"a": "1", "b": "", "c": "3"}
        result = drop_empty(original)
        self.assertEqual(original, {"a": "1", "b": "", "c": "3"})
        self.assertEqual(result, {"a": "1", "c": "3"})


if __name__ == "__main__":
    unittest.main()
