def sum_of_multiples(n: int, k: int) -> int:
    """Return the sum of the positive multiples of k that are less than n.
    
    Returns 0 when k <= 0.
    """
    if k <= 0:
        return 0
    return sum(i for i in range(k, n, k))
