def collatz_steps(n: int) -> int:
    """Return the number of steps to reach 1 using the Collatz rule.

    The Collatz rule: if n is even, divide by 2; if odd, compute 3n+1.
    For n <= 1, returns 0.
    """
    if n <= 1:
        return 0
    
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    
    return steps
