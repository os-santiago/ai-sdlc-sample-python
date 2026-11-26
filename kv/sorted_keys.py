def sorted_keys(m: dict[str, str] | None) -> list[str]:
    """Return the keys of m in ascending order; None or an empty map gives []."""
    if not m:
        return []
    return sorted(m)
