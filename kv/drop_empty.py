def drop_empty(m: dict[str, str]) -> dict[str, str]:
    """Return a new dict without the entries whose value is an empty string."""
    return {k: v for k, v in m.items() if v != ""}
