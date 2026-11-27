def alternate_case(s: str) -> str:
    """Return s with characters at even indexes upper-cased and odd indexes lower-cased."""
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return "".join(result)
