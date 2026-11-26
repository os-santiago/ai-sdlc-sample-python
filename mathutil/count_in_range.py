def count_in_range(xs: list[int], lo: int, hi: int) -> int:
    """Count values in the closed range [lo, hi].

    Returns 0 when lo > hi.
    """
    if lo > hi:
        return 0
    return sum(1 for x in xs if lo <= x <= hi)
