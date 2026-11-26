def factorial(n: int) -> int:
    """Return the factorial of n (n!).

    factorial(0) == 1
    For negative n, raises ValueError.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
