def max_gap(xs: list[int]) -> int:
    """Return the largest gap between consecutive values after sorting.
    
    Returns 0 if xs has fewer than two values.
    """
    if len(xs) < 2:
        return 0
    
    sorted_xs = sorted(xs)
    max_diff = 0
    
    for i in range(1, len(sorted_xs)):
        diff = sorted_xs[i] - sorted_xs[i - 1]
        if diff > max_diff:
            max_diff = diff
    
    return max_diff
