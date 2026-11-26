def min_key(m: dict[str, str]) -> str | None:
    """Return the lexically smallest key, or None for an empty dict."""
    if not m:
        return None
    return min(m)
