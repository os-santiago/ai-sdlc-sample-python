def swap_case_values(m: dict[str, str]) -> dict[str, str]:
    """Return a new dict with each value's case swapped.

    Returns a new dictionary with the same keys as m, but with each value
    having its case swapped (uppercase becomes lowercase and vice versa).
    The input dictionary is not modified.
    """
    return {key: value.swapcase() for key, value in m.items()}
