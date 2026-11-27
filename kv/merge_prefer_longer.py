def merge_prefer_longer(a: dict[str, str], b: dict[str, str]) -> dict[str, str]:
    """Return a new dict with every key of a and b; longer values win.
    
    For keys in both dicts, the longer value is chosen.
    If values have equal length, a's value wins.
    """
    result = dict(a)
    for key, b_value in b.items():
        if key not in result or len(b_value) > len(result[key]):
            result[key] = b_value
    return result
