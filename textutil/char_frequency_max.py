def char_frequency_max(s: str) -> str:
    """Return the character that appears most often in s (the earliest such character on ties), or an empty string for empty input."""
    if not s:
        return ""
    
    # Count frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find max frequency
    max_freq = max(freq.values())
    
    # Find the first character in s with max frequency
    for char in s:
        if freq[char] == max_freq:
            return char
    
    return ""  # Should never reach here
