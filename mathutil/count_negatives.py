def count_negatives(xs: list[int]) -> int:
    """Count values below zero.

    Returns the number of negative values in the list.
    """
    return sum(1 for x in xs if x < 0)
