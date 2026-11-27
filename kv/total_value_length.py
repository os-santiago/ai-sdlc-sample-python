def total_value_length(m: dict[str, str]) -> int:
    """Return the sum of the lengths of all values in m."""
    return sum(len(value) for value in m.values())
