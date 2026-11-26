def count_divisors(n: int) -> int:
    """Count the number of positive divisors of n.
    
    Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            # i is a divisor
            count += 1
            # n // i is also a divisor (if different from i)
            if i * i != n:
                count += 1
        i += 1
    return count
