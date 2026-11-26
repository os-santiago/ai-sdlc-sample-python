import unittest
from textutil.hanging_indent import hanging_indent


class TestHangingIndent(unittest.TestCase):
    def test_single_line(self):
        """Test that a single line is returned unchanged."""
        result = hanging_indent("Hello world", 4)
        self.assertEqual(result, "Hello world")

    def test_multiple_lines(self):
        """Test that lines after the first are indented."""
        text = "First line\nSecond line\nThird line"
        result = hanging_indent(text, 4)
        expected = "First line\n    Second line\n    Third line"
        self.assertEqual(result, expected)

    def test_n_zero(self):
        """Test that n=0 returns the string unchanged."""
        text = "First line\nSecond line"
        result = hanging_indent(text, 0)
        self.assertEqual(result, text)

    def test_n_negative(self):
        """Test that negative n returns the string unchanged."""
        text = "First line\nSecond line"
        result = hanging_indent(text, -5)
        self.assertEqual(result, text)

    def test_various_indent_sizes(self):
        """Test different indent sizes."""
        text = "Line 1\nLine 2"
        
        result_2 = hanging_indent(text, 2)
        self.assertEqual(result_2, "Line 1\n  Line 2")
        
        result_8 = hanging_indent(text, 8)
        self.assertEqual(result_8, "Line 1\n        Line 2")

    def test_empty_lines(self):
        """Test handling of empty lines in the middle."""
        text = "First\n\nThird"
        result = hanging_indent(text, 2)
        expected = "First\n  \n  Third"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
