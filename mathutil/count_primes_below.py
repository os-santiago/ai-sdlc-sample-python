def count_primes_below(n: int) -> int:
    """Count primes p with 2 <= p < n."""
    count = 0
    for candidate in range(2, n):
        if is_prime_local(candidate):
            count += 1
    return count


def is_prime_local(num: int) -> bool:
    """Check if num is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True
