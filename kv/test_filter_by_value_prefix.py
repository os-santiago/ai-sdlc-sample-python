import unittest

from kv import filter_by_value_prefix


class FilterByValuePrefixTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(filter_by_value_prefix({}, "pre"), {})

    def test_no_match(self):
        m = {"a": "apple", "b": "banana", "c": "cherry"}
        self.assertEqual(filter_by_value_prefix(m, "x"), {})

    def test_several_matches(self):
        m = {"a": "apple", "b": "apricot", "c": "banana", "d": "avocado"}
        self.assertEqual(filter_by_value_prefix(m, "a"), {"a": "apple", "b": "apricot", "d": "avocado"})

    def test_single_match(self):
        m = {"a": "apple", "b": "banana"}
        self.assertEqual(filter_by_value_prefix(m, "b"), {"b": "banana"})

    def test_all_match(self):
        m = {"a": "apple", "b": "apricot"}
        self.assertEqual(filter_by_value_prefix(m, "a"), {"a": "apple", "b": "apricot"})


if __name__ == "__main__":
    unittest.main()
