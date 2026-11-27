import unittest

from kv import has_any


class HasAnyTest(unittest.TestCase):
    def test_empty_keys(self):
        self.assertFalse(has_any({"a": "1"}, []))

    def test_no_match(self):
        self.assertFalse(has_any({"a": "1", "b": "2"}, ["x", "y"]))
        self.assertFalse(has_any({"a": "1"}, ["x"]))
        self.assertFalse(has_any({}, ["a"]))

    def test_one_match(self):
        self.assertTrue(has_any({"a": "1", "b": "2"}, ["a"]))
        self.assertTrue(has_any({"a": "1"}, ["a"]))
        self.assertTrue(has_any({"a": "1", "b": "2", "c": "3"}, ["x", "b", "y"]))


if __name__ == "__main__":
    unittest.main()
