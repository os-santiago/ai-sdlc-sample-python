def longest_word(s: str) -> str:
    """Return the first word with the most characters, or an empty string for blank input."""
    words = s.split()
    if not words:
        return ""
    
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest
