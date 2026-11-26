def pick(m: dict[str, str] | None, keys: list[str]) -> dict[str, str]:
    """Return a new map with only the entries of m whose key is in keys.

    Missing keys are ignored; None counts as an empty map.
    """
    if not m:
        return {}
    return {k: m[k] for k in keys if k in m}
