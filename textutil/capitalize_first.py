def capitalize_first(s: str) -> str:
    """Capitalize the first letter of s, leaving the rest unchanged."""
    if not s:
        return ""
    return s[0].upper() + s[1:]
