def sum_range(lo: int, hi: int) -> int:
    """Return the sum of the integers from lo to hi inclusive, or 0 when lo > hi."""
    if lo > hi:
        return 0
    return (lo + hi) * (hi - lo + 1) // 2
