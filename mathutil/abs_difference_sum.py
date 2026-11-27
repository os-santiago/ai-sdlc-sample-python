def abs_difference_sum(xs: list[int]) -> int:
    """Return the sum of absolute differences between consecutive pairs."""
    if len(xs) < 2:
        return 0
    return sum(abs(xs[i+1] - xs[i]) for i in range(len(xs) - 1))
