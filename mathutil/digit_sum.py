def digit_sum(n: int) -> int:
    """Return the sum of the decimal digits of abs(n)."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
