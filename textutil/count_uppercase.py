def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s."""
    return sum(1 for char in s if char.isupper())
