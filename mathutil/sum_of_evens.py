def sum_of_evens(xs: list[int]) -> int:
    """Return the sum of the even values in xs."""
    return sum(x for x in xs if x % 2 == 0)
