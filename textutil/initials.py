def initials(s: str) -> str:
    """Return the upper-cased first character of each whitespace-separated word.

    Returns a string with no separators between the initials.
    """
    return "".join(word[:1].upper() for word in s.split())
