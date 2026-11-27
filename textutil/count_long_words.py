def count_long_words(s: str, n: int) -> int:
    """Return the number of whitespace-separated words with at least n characters."""
    words = s.split()
    return sum(1 for word in words if len(word) >= n)
