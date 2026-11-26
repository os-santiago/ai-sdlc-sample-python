import unittest

from kv import pick


class PickTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(pick(None, ["a"]), {})

    def test_subset(self):
        self.assertEqual(pick({"a": "1", "b": "2", "c": "3"}, ["a", "c"]), {"a": "1", "c": "3"})

    def test_missing_keys(self):
        self.assertEqual(pick({"a": "1"}, ["x", "a"]), {"a": "1"})


if __name__ == "__main__":
    unittest.main()
