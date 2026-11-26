def vowel_count(s: str) -> int:
    """Return the number of ASCII vowels (a, e, i, o, u) in s, ignoring case."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
