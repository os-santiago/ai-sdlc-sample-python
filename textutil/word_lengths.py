def word_lengths(s: str) -> list[int]:
    """Return the length of each whitespace-separated word in s."""
    return [len(word) for word in s.split()]
