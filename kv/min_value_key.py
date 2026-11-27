def min_value_key(m: dict[str, int]) -> str | None:
    """Return the key with the smallest value (smallest key on ties), or None for an empty dict."""
    if not m:
        return None
    min_val = min(m.values())
    # Find all keys with min value, return the smallest one
    return min(k for k, v in m.items() if v == min_val)
