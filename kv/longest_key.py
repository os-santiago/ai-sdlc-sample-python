def longest_key(m: dict[str, str]) -> str | None:
    """Return the longest key (the smallest such key on ties), or None for an empty dict."""
    if not m:
        return None
    return sorted(m, key=lambda k: (-len(k), k))[0]
