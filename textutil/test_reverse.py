import unittest

from textutil import reverse


class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(""), "")

    def test_ascii(self):
        self.assertEqual(reverse("abc"), "cba")

    def test_unicode(self):
        self.assertEqual(reverse("café"), "éfac")


if __name__ == "__main__":
    unittest.main()
