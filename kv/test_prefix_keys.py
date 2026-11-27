import unittest

from kv import prefix_keys


class PrefixKeysTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(prefix_keys({}, "pre"), {})

    def test_empty_prefix(self):
        m = {"a": "1", "b": "2"}
        self.assertEqual(prefix_keys(m, ""), {"a": "1", "b": "2"})

    def test_normal_prefix(self):
        m = {"a": "1", "b": "2"}
        self.assertEqual(prefix_keys(m, "pre_"), {"pre_a": "1", "pre_b": "2"})

    def test_none_input(self):
        self.assertEqual(prefix_keys(None, "pre"), {})

    def test_prefix_multiple_keys(self):
        m = {"foo": "value1", "bar": "value2", "baz": "value3"}
        self.assertEqual(prefix_keys(m, "new_"), {"new_foo": "value1", "new_bar": "value2", "new_baz": "value3"})


if __name__ == "__main__":
    unittest.main()
