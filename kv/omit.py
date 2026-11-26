def omit(m: dict[str, str] | None, keys: list[str]) -> dict[str, str]:
    """Return a new map without the entries whose key is in keys.

    Missing keys are ignored; None counts as an empty map.
    """
    if not m:
        return {}
    return {k: v for k, v in m.items() if k not in keys}
