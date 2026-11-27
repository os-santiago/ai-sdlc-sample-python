def vowel_ratio_percent(s: str) -> int:
    """Return the integer floor of 100 times the number of ASCII vowels divided by the number of ASCII letters in s."""
    vowels = "aeiouAEIOU"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    vowel_count = sum(1 for char in s if char in vowels)
    letter_count = sum(1 for char in s if char in letters)
    
    if letter_count == 0:
        return 0
    
    return int(100 * vowel_count / letter_count)
