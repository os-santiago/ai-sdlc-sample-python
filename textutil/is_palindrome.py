def is_palindrome(s: str) -> bool:
    """Report whether s reads the same backwards, ignoring case and non-alphanumeric characters."""
    chars = [c.casefold() for c in s if c.isalnum()]
    return chars == chars[::-1]
