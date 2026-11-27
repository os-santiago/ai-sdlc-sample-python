def prefix_keys(m: dict[str, str], prefix: str) -> dict[str, str]:
    """Return a new dict with prefix added to the start of every key.

    An empty prefix leaves keys unchanged; None counts as an empty map.
    """
    if not m:
        return {}
    if not prefix:
        return dict(m)
    return {prefix + k: v for k, v in m.items()}
