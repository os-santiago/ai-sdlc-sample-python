def capitalize_words(s: str) -> str:
    """Upper-case the first character of each whitespace-separated word.

    The rest of each word is kept; single spaces separate words in the result.
    """
    return " ".join(word[:1].upper() + word[1:] for word in s.split())
