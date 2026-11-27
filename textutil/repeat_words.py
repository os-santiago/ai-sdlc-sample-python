def repeat_words(s: str, n: int) -> str:
    """Repeat each whitespace-separated word n times.

    Words are joined by single spaces. If n <= 0, returns an empty string.
    """
    if n <= 0:
        return ""
    
    words = s.split()
    repeated = []
    for word in words:
        repeated.extend([word] * n)
    return " ".join(repeated)
