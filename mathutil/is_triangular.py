def is_triangular(n: int) -> bool:
    """Report whether n equals k*(k+1)/2 for some integer k >= 1."""
    if n < 1:
        return False
    
    # Solve k^2 + k - 2n = 0 using quadratic formula
    # k = (-1 + sqrt(1 + 8n)) / 2
    discriminant = 1 + 8 * n
    
    # Check if discriminant is a perfect square
    sqrt_discriminant = int(discriminant ** 0.5)
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False
    
    # Check if k would be an integer
    if (sqrt_discriminant - 1) % 2 != 0:
        return False
    
    k = (sqrt_discriminant - 1) // 2
    
    # Verify the result (k >= 1 is guaranteed by n >= 1 check)
    return k * (k + 1) // 2 == n
