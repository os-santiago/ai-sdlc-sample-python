import unittest

from kv import swap_case_values


class SwapCaseValuesTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(swap_case_values({}), {})

    def test_mixed_case_values(self):
        self.assertEqual(
            swap_case_values({"a": "Hello", "b": "WORLD", "c": "Python"}),
            {"a": "hELLO", "b": "world", "c": "pYTHON"}
        )

    def test_input_unchanged(self):
        original = {"x": "Test", "y": "DATA"}
        expected_original = {"x": "Test", "y": "DATA"}
        result = swap_case_values(original)
        # Verify input is unchanged
        self.assertEqual(original, expected_original)
        # Verify result is correct
        self.assertEqual(result, {"x": "tEST", "y": "data"})

    def test_all_uppercase(self):
        self.assertEqual(swap_case_values({"a": "ABC"}), {"a": "abc"})

    def test_all_lowercase(self):
        self.assertEqual(swap_case_values({"b": "xyz"}), {"b": "XYZ"})


if __name__ == "__main__":
    unittest.main()
