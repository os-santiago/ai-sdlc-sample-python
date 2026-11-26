import unittest

from kv import has_all


class HasAllTest(unittest.TestCase):
    def test_none(self):
        self.assertFalse(has_all(None, ["a"]))

    def test_empty_keys(self):
        self.assertTrue(has_all({"a": "1"}, []))
        self.assertTrue(has_all(None, []))

    def test_all_present(self):
        self.assertTrue(has_all({"a": "1", "b": "2", "c": "3"}, ["a", "c"]))
        self.assertTrue(has_all({"a": "1"}, ["a"]))

    def test_one_missing(self):
        self.assertFalse(has_all({"a": "1", "b": "2"}, ["a", "c"]))
        self.assertFalse(has_all({"a": "1"}, ["x"]))


if __name__ == "__main__":
    unittest.main()
