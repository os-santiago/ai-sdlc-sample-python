def invert(m: dict[str, str] | None) -> dict[str, str]:
    """Return a new map from each value of m to its key.

    When several keys share a value, the lexically smallest key wins.
    """
    result: dict[str, str] = {}
    for key in sorted(m or {}, reverse=True):
        result[m[key]] = key
    return result
