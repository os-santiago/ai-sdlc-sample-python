import unittest

from kv import values_with_prefix


class ValuesWithPrefixTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(values_with_prefix({}, "pre"), [])

    def test_no_match(self):
        m = {"apple": "1", "banana": "2", "cherry": "3"}
        self.assertEqual(values_with_prefix(m, "x"), [])

    def test_several_matches_in_key_order(self):
        m = {"foo_z": "last", "foo_a": "first", "bar_c": "ignored", "foo_m": "middle"}
        self.assertEqual(values_with_prefix(m, "foo_"), ["first", "middle", "last"])

    def test_single_match(self):
        m = {"prefix_a": "match", "other_b": "no"}
        self.assertEqual(values_with_prefix(m, "prefix_"), ["match"])

    def test_all_keys_match(self):
        m = {"pre_c": "3", "pre_a": "1", "pre_b": "2"}
        self.assertEqual(values_with_prefix(m, "pre_"), ["1", "2", "3"])


if __name__ == "__main__":
    unittest.main()
