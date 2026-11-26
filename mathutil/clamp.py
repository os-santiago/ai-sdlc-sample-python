def clamp(n: int, lo: int, hi: int) -> int:
    """Return n limited to the inclusive range [lo, hi].

    Raises ValueError when lo > hi.
    """
    if lo > hi:
        raise ValueError("lo must not exceed hi")
    return max(lo, min(n, hi))
