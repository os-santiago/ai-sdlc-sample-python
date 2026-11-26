def merge(a: dict[str, str] | None, b: dict[str, str] | None) -> dict[str, str]:
    """Return a new map with the entries of a and b; b wins on shared keys.

    Neither input is modified; None counts as an empty map.
    """
    result = dict(a or {})
    result.update(b or {})
    return result
