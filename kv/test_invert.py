import unittest

from kv import invert


class InvertTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual(invert(None), {})

    def test_unique(self):
        self.assertEqual(invert({"a": "1", "b": "2"}), {"1": "a", "2": "b"})

    def test_shared_value(self):
        self.assertEqual(invert({"b": "x", "a": "x", "c": "y"}), {"x": "a", "y": "c"})


if __name__ == "__main__":
    unittest.main()
