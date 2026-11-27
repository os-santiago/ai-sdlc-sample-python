def upper_keys(m: dict[str, str]) -> dict[str, str]:
    """Return a new dict with all keys upper-cased.

    On collisions, the value of the lexically largest original key wins.
    """
    result: dict[str, str] = {}
    for key in sorted(m):
        result[key.upper()] = m[key]
    return result
