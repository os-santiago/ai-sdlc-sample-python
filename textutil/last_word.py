def last_word(s: str) -> str:
    """Return the last whitespace-separated word of s, or an empty string for blank input."""
    words = s.split()
    if not words:
        return ""
    return words[-1]
