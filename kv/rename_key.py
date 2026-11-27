def rename_key(m: dict[str, str], old: str, new: str) -> dict[str, str]:
    """Return a copy of m with key old renamed to new.

    If old is not in m, returns an unchanged copy.
    The input dict is never modified.
    """
    result = m.copy()
    if old in result:
        result[new] = result.pop(old)
    return result
