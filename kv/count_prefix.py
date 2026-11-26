def count_prefix(m: dict[str, str], prefix: str) -> int:
    """Count keys that start with prefix.

    An empty prefix counts every key.
    """
    if not m:
        return 0
    if not prefix:
        return len(m)
    return sum(1 for k in m if k.startswith(prefix))
