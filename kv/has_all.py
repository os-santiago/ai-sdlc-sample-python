def has_all(m: dict[str, str] | None, keys: list[str]) -> bool:
    """Return whether every key in keys is present in m.

    An empty keys list returns True; None counts as an empty map.
    """
    if not keys:
        return True
    if not m:
        return False
    return all(k in m for k in keys)
