def count_consonants(s: str) -> int:
    """Return the number of ASCII consonants in s (letters that are not vowels)."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)
