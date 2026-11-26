def filter_prefix(m: dict[str, str] | None, prefix: str) -> dict[str, str]:
    """Return a new map with only the entries whose key starts with prefix.

    An empty prefix keeps every entry; None counts as an empty map.
    """
    if not m:
        return {}
    if not prefix:
        return dict(m)
    return {k: v for k, v in m.items() if k.startswith(prefix)}
