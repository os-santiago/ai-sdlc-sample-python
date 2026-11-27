import unittest

from kv import merge_prefer_longer


class MergePreferLongerTest(unittest.TestCase):
    def test_empty_dicts(self):
        self.assertEqual(merge_prefer_longer({}, {}), {})
        self.assertEqual(merge_prefer_longer({"a": "1"}, {}), {"a": "1"})
        self.assertEqual(merge_prefer_longer({}, {"b": "2"}), {"b": "2"})

    def test_disjoint_keys(self):
        self.assertEqual(
            merge_prefer_longer({"a": "1"}, {"b": "2"}),
            {"a": "1", "b": "2"}
        )
        self.assertEqual(
            merge_prefer_longer({"a": "1", "b": "2"}, {"c": "3", "d": "4"}),
            {"a": "1", "b": "2", "c": "3", "d": "4"}
        )

    def test_shared_keys_b_longer(self):
        self.assertEqual(
            merge_prefer_longer({"a": "1"}, {"a": "123"}),
            {"a": "123"}
        )
        self.assertEqual(
            merge_prefer_longer({"a": "x", "b": "y"}, {"a": "xxx"}),
            {"a": "xxx", "b": "y"}
        )

    def test_shared_keys_a_longer(self):
        self.assertEqual(
            merge_prefer_longer({"a": "123"}, {"a": "1"}),
            {"a": "123"}
        )
        self.assertEqual(
            merge_prefer_longer({"a": "xxx", "b": "y"}, {"a": "x"}),
            {"a": "xxx", "b": "y"}
        )

    def test_shared_keys_equal_length(self):
        # a wins on equal length
        self.assertEqual(
            merge_prefer_longer({"a": "12"}, {"a": "34"}),
            {"a": "12"}
        )
        self.assertEqual(
            merge_prefer_longer({"a": "abc"}, {"a": "xyz"}),
            {"a": "abc"}
        )

    def test_multiple_keys_mixed(self):
        self.assertEqual(
            merge_prefer_longer(
                {"a": "1", "b": "long", "c": "same"},
                {"a": "longer", "c": "same", "d": "3"}
            ),
            {"a": "longer", "b": "long", "c": "same", "d": "3"}
        )

    def test_inputs_unchanged(self):
        a, b = {"a": "1"}, {"b": "2"}
        merge_prefer_longer(a, b)
        self.assertEqual(a, {"a": "1"})
        self.assertEqual(b, {"b": "2"})


if __name__ == "__main__":
    unittest.main()
