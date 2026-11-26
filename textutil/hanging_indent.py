def hanging_indent(s: str, n: int) -> str:
    """Indent every line after the first by n spaces.
    
    Args:
        s: The input string
        n: Number of spaces to indent (n <= 0 returns s unchanged)
    
    Returns:
        String with hanging indentation applied
    """
    if n <= 0:
        return s
    
    lines = s.split('\n')
    if len(lines) <= 1:
        return s
    
    indent = ' ' * n
    return lines[0] + '\n' + '\n'.join(indent + line for line in lines[1:])
