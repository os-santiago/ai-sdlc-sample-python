def mean_int(xs: list[int]) -> int:
    """Return the floor of the arithmetic mean of xs, or 0 for an empty list."""
    if not xs:
        return 0
    return sum(xs) // len(xs)
