import unittest

from kv import total_value_length


class TotalValueLengthTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(total_value_length({}), 0)

    def test_empty_values(self):
        self.assertEqual(total_value_length({"a": "", "b": ""}), 0)

    def test_several_values(self):
        self.assertEqual(total_value_length({"a": "hi", "b": "bye", "c": "x"}), 6)

    def test_single_value(self):
        self.assertEqual(total_value_length({"key": "hello"}), 5)


if __name__ == "__main__":
    unittest.main()
