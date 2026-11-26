def is_power_of_two(n: int) -> bool:
    """Report whether n is a positive power of two."""
    return n > 0 and (n & (n - 1)) == 0
