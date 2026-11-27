def first_char(s: str) -> str:
    """Return the first character of s that is not whitespace, or an empty string if there is none."""
    for char in s:
        if not char.isspace():
            return char
    return ""
