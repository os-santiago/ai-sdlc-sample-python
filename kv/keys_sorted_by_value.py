def keys_sorted_by_value(m: dict[str, str]) -> list[str]:
    """Return the keys ordered by their value, then by key for equal values."""
    if not m:
        return []
    return sorted(m.keys(), key=lambda k: (m[k], k))
