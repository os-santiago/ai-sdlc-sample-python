def to_snake_case(s: str) -> str:
    """Lower-case whitespace-separated words and join with underscores.

    Multiple spaces are collapsed; leading/trailing spaces are removed.
    """
    return "_".join(word.lower() for word in s.split())
