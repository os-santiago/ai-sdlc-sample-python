def values_with_prefix(m: dict[str, str], prefix: str) -> list[str]:
    """Return values whose keys start with prefix, ordered by key.

    Returns an empty list if the map is empty or no keys match.
    """
    if not m:
        return []
    # Filter keys that start with prefix, sort them, then get their values
    matching_keys = sorted(k for k in m.keys() if k.startswith(prefix))
    return [m[k] for k in matching_keys]
