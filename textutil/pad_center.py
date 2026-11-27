def pad_center(s: str, width: int, fill: str = " ") -> str:
    """Center s in width using fill, putting any extra fill on the right."""
    if width <= len(s):
        return s
    
    total_padding = width - len(s)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    
    return fill * left_padding + s + fill * right_padding
