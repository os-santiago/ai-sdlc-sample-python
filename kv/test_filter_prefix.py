import unittest

from kv import filter_prefix


class FilterPrefixTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(filter_prefix(None, "pre"), {})

    def test_empty_prefix(self):
        m = {"a": "1", "b": "2", "c": "3"}
        self.assertEqual(filter_prefix(m, ""), {"a": "1", "b": "2", "c": "3"})

    def test_prefix_matches_some(self):
        m = {"foo_a": "1", "foo_b": "2", "bar_c": "3"}
        self.assertEqual(filter_prefix(m, "foo_"), {"foo_a": "1", "foo_b": "2"})

    def test_prefix_matches_none(self):
        m = {"a": "1", "b": "2"}
        self.assertEqual(filter_prefix(m, "x"), {})

    def test_prefix_matches_all(self):
        m = {"foo_a": "1", "foo_b": "2"}
        self.assertEqual(filter_prefix(m, "foo_"), {"foo_a": "1", "foo_b": "2"})


if __name__ == "__main__":
    unittest.main()
