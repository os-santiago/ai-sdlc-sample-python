def digit_product(n: int) -> int:
    """Return the product of the decimal digits of abs(n)."""
    n = abs(n)
    if n == 0:
        return 0
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product
