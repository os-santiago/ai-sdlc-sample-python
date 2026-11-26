def is_perfect(n: int) -> bool:
    """Report whether n is a perfect number.
    
    A perfect number equals the sum of its positive divisors excluding itself.
    Numbers <= 1 are not perfect.
    """
    if n <= 1:
        return False
    
    # Sum of divisors excluding n itself
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum == n
