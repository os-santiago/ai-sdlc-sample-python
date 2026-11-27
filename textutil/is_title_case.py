def is_title_case(s: str) -> bool:
    """Report whether s is non-empty and every whitespace-separated word starts with an uppercase letter."""
    if not s:
        return False
    words = s.split()
    return bool(words) and all(word[0].isupper() for word in words)
