def next_multiple(n: int, step: int) -> int:
    """Return the smallest multiple of step that is >= n.

    When step <= 0, returns n unchanged.
    """
    if step <= 0:
        return n
    remainder = n % step
    if remainder == 0:
        return n
    return n + (step - remainder)
