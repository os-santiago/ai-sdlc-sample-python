from kv.key_count_with_value import key_count_with_value


def test_empty_dict():
    """Empty dict returns 0."""
    assert key_count_with_value({}, "any") == 0


def test_no_match():
    """No keys have the target value."""
    m = {"a": "1", "b": "2", "c": "3"}
    assert key_count_with_value(m, "4") == 0


def test_several_matches():
    """Several keys have the target value."""
    m = {"a": "x", "b": "y", "c": "x", "d": "x"}
    assert key_count_with_value(m, "x") == 3


def test_single_match():
    """Single key has the target value."""
    m = {"a": "1", "b": "2", "c": "3"}
    assert key_count_with_value(m, "2") == 1


def test_all_match():
    """All keys have the target value."""
    m = {"a": "same", "b": "same", "c": "same"}
    assert key_count_with_value(m, "same") == 3
