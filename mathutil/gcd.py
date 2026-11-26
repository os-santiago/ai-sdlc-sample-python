def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b, always non-negative.

    gcd(0, 0) is 0.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
