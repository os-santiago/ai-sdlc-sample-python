from textutil.truncate import truncate


def test_truncate_zero_length():
    """Test truncate with n=0 returns empty string."""
    assert truncate("hello", 0) == ""
    assert truncate("", 0) == ""


def test_truncate_negative_length():
    """Test truncate with n<0 returns empty string."""
    assert truncate("hello", -1) == ""
    assert truncate("world", -10) == ""


def test_truncate_short_string():
    """Test truncate with short string returns unchanged."""
    assert truncate("hi", 5) == "hi"
    assert truncate("hello", 5) == "hello"
    assert truncate("world", 10) == "world"
    assert truncate("", 5) == ""


def test_truncate_exact_length():
    """Test truncate when string length equals n."""
    assert truncate("hello", 5) == "hello"
    assert truncate("ab", 2) == "ab"


def test_truncate_long_string():
    """Test truncate with long string adds ellipsis."""
    assert truncate("hello world", 5) == "hello..."
    assert truncate("this is a very long string", 10) == "this is a ..."
    assert truncate("abcdefghij", 3) == "abc..."
