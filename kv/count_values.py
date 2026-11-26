def count_values(m: dict[str, str] | None) -> dict[str, int]:
    """Return a map from each value of m to how many keys map to it."""
    result: dict[str, int] = {}
    for value in (m or {}).values():
        result[value] = result.get(value, 0) + 1
    return result
