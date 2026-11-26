def remove_vowels(s: str) -> str:
    """Return s without ASCII vowels (a, e, i, o, u in either case)."""
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)
