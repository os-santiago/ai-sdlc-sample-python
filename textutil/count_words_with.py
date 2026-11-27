def count_words_with(s: str, ch: str) -> int:
    """Return the number of whitespace-separated words that contain the character ch (case-sensitive)."""
    words = s.split()
    return sum(1 for word in words if ch in word)
