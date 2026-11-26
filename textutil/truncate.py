def truncate(s: str, n: int) -> str:
    """Return s truncated to n characters with '...' suffix if longer.
    
    Args:
        s: The string to truncate
        n: Maximum length before truncation
        
    Returns:
        - Empty string if n <= 0
        - s unchanged if len(s) <= n
        - First n characters of s followed by "..." if len(s) > n
    """
    if n <= 0:
        return ""
    if len(s) <= n:
        return s
    return s[:n] + "..."
