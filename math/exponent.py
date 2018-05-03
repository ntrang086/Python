"""Implement an exponent function in log(n) time."""

def power_recursively(a, n):
    """Calculate a to the power of n using recursion.
    https://en.wikipedia.org/wiki/Exponentiation_by_squaring
    """
    if n < 0:
        return power_recursively(1 / a, -n)
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return power_recursively(a * a, int(n / 2))
    return a * power_recursively(a * a, int(n / 2))

def power_iteratively(a, n):
    """Calculate a to the power of n using iteration.
    https://en.wikipedia.org/wiki/Exponentiation_by_squaring
    """
    if n < 0:
        a = 1 / a
        n = -n
    if n == 0:
        return 1
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n = int(n / 2)
    return result


if __name__ == "__main__":
    assert power_recursively(2, 9) == 512
    assert power_iteratively(2, 9) == 512