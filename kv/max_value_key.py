def max_value_key(m: dict[str, int]) -> str | None:
    """Return the key with the largest value (smallest key on ties), or None for an empty dict."""
    if not m:
        return None
    max_val = max(m.values())
    # Find all keys with max value, return the smallest one
    return min(k for k, v in m.items() if v == max_val)
