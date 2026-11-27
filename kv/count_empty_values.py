def count_empty_values(m: dict[str, str]) -> int:
    """Count the keys whose value is an empty string."""
    count = 0
    for value in m.values():
        if value == "":
            count += 1
    return count
