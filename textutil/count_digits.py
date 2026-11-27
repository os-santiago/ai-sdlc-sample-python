def count_digits(s: str) -> int:
    """Return the number of digit characters in s."""
    return sum(1 for char in s if char.isdigit())
