def is_square_sum(n: int) -> bool:
    """Report whether n equals a*a + b*b for some integers a, b >= 0."""
    if n < 0:
        return False
    
    # Check all possible values of a from 0 to sqrt(n)
    a = 0
    while a * a <= n:
        b_squared = n - a * a
        # Check if b_squared is a perfect square
        b = int(b_squared ** 0.5)
        if b * b == b_squared:
            return True
        a += 1
    
    return False
