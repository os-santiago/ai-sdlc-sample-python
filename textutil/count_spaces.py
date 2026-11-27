def count_spaces(s: str) -> int:
    """Return the number of space characters in s."""
    return sum(1 for char in s if char == ' ')
