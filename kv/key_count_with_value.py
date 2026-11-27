def key_count_with_value(m: dict[str, str], value: str) -> int:
    """Count keys whose value equals the given value.

    Returns 0 for an empty dict.
    """
    if not m:
        return 0
    return sum(1 for v in m.values() if v == value)
