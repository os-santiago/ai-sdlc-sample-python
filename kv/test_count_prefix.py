from kv.count_prefix import count_prefix


def test_empty_dict():
    """Empty dict returns 0."""
    assert count_prefix({}, "any") == 0


def test_empty_prefix():
    """Empty prefix counts all keys."""
    m = {"a": "1", "b": "2", "c": "3"}
    assert count_prefix(m, "") == 3


def test_prefix_matching_some():
    """Prefix matching some keys."""
    m = {"app_name": "1", "app_version": "2", "db_host": "3"}
    assert count_prefix(m, "app") == 2


def test_prefix_matching_none():
    """Prefix matching no keys."""
    m = {"a": "1", "b": "2"}
    assert count_prefix(m, "x") == 0


def test_prefix_matching_all():
    """Prefix matching all keys."""
    m = {"app_name": "1", "app_version": "2"}
    assert count_prefix(m, "app") == 2
