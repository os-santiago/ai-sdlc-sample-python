from mathutil.gcd import gcd


def lcm(a: int, b: int) -> int:
    """Return the non-negative least common multiple of a and b.

    Returns 0 when either a or b is 0.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
