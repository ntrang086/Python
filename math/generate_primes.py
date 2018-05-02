"""Generate the first n prime numbers."""

def generate_primes(n):
    """Generate all primes <= n using the sieve of Eratosthenes.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.
    """
    if n < 2:
        return set()
    # Create a set of consecutive integers from 2 to n (inclusive)
    primes = set([i for i in range(2, n + 1)])
    # Initially, let p equal 2, the smallest prime number
    p = 2
    # When p * p is > n, stop the while loop because all the multiples,
    # of p which are also multiples of smaller primes, have been removed 
    while p * p <= n:
        # If p hasn't been removed from primes in the below for loop, it is a prime
        if p in primes:
            # Enumerate the multiples of p by counting to n from 2p 
            # in increments of p, and remove them from the primes set
            for i in range(p * 2, n + 1, p):
                if i in primes:
                    primes.remove(i)
        # Increment p until the first number greater than p has not been 
        # removed from the above for loop. If there was no such number, stop. 
        # Otherwise, let p now equal this new number (which is the next prime)
        p += 1
    return primes

if __name__ == "__main__":
    # Generate primes using the sieve of Eratosthenes
    assert generate_primes(10) == {2, 3, 5, 7}
    assert generate_primes(15) == {2, 3, 5, 7, 11, 13}
    assert generate_primes(200) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199}