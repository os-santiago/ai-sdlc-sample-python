import string


def strip_punctuation(s: str) -> str:
    """Return s without ASCII punctuation characters."""
    return ''.join(char for char in s if char not in string.punctuation)
