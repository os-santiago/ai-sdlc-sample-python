def has_any(m: dict[str, str], keys: list[str]) -> bool:
    """Return whether at least one key in keys is present in m.

    An empty keys list returns False.
    """
    if not keys:
        return False
    return any(k in m for k in keys)
