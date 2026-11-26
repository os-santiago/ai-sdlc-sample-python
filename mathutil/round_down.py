def round_down(n: int, step: int) -> int:
    """Return the largest multiple of step that is <= n.

    When step <= 0, returns n unchanged.
    """
    if step <= 0:
        return n
    return (n // step) * step
