from mathutil.clamp import clamp


def clamp_list(xs: list[int], lo: int, hi: int) -> list[int]:
    """Return a new list with each value clamped to [lo, hi].

    Raises ValueError when lo > hi.
    """
    if lo > hi:
        raise ValueError("lo must not exceed hi")
    return [clamp(x, lo, hi) for x in xs]
