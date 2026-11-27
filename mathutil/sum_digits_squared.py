def sum_digits_squared(n: int) -> int:
    """Return the sum of the squares of the decimal digits of abs(n)."""
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total
