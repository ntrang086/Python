"""Check if a number is a prime."""

def is_prime_simple(n):
    """Check if a number is a prime.
    - Check till sqrt(n) because a larger factor of n must be a 
    multiple of smaller factor that has been already checked.
    - All primes are of the form 6k ± 1, with the exception of 
    2 and 3. So test if n is divisible by 2 or 3, then to check 
    through all the numbers of form 6k ± 1. 
    https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    p = 5
    while p * p <= n:
        if n % p == 0 or n % (p + 2) == 0:
            return False
        p += 6
    return True


if __name__ == "__main__":
    # Test is_prime_simple
    assert all(is_prime_simple(i) for i in [2, 3, 5, 7, 11]) == True
    assert all(is_prime_simple(i) for i in [1, 4, 6, 8, 9, 10]) == False