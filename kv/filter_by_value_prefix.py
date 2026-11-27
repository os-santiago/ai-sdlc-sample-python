def filter_by_value_prefix(m: dict[str, str], prefix: str) -> dict[str, str]:
    """Return a new dict with entries whose value starts with prefix.

    Returns an empty dict if the input is empty or no values match.
    """
    if not m:
        return {}
    return {k: v for k, v in m.items() if v.startswith(prefix)}
