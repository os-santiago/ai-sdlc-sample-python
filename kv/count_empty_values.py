def count_empty_values(m: dict[str, str]) -> int:
    """Count the keys whose value is an empty string."""
    return sum(1 for value in m.values() if value == "")
