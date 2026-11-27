def is_palindrome_number(n: int) -> bool:
    """Report whether the decimal digits of n read the same backwards.
    
    Negative numbers are never palindromes.
    """
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]
