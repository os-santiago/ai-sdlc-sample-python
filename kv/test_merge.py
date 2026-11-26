import unittest

from kv import merge


class MergeTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(merge(None, None), {})
        self.assertEqual(merge({"a": "1"}, None), {"a": "1"})

    def test_right_wins(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": "3"}), {"a": "1", "b": "3"})

    def test_inputs_unchanged(self):
        a, b = {"a": "1"}, {"b": "2"}
        merge(a, b)
        self.assertEqual(a, {"a": "1"})
        self.assertEqual(b, {"b": "2"})


if __name__ == "__main__":
    unittest.main()
