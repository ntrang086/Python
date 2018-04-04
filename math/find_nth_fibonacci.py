"""Write a function that returns the nth number in Fibonacci sequences with an input n."""

import timeit

def fibonacci_recursively(n):
    """Return the nth number in the Fibonacci's sequence.
    If n <= 1, return n. If n > 1, return F(n-1) + F(n-2).
    Use recursion.
    """
    if n <= 1:
        return n
    return fibonacci_recursively(n - 1) + fibonacci_recursively(n - 2)
 
def fibonacci_iteratively(n):
    """Return the nth number in the Fibonacci's sequence.
    If n <= 1, return n. If n > 1, return F(n-1) + F(n-2).
    Use iteration.
    """
    if n <= 1:
        return n
    prev = 0
    curr = 1
    result = 1
    for i in range(2, n + 1):
        result = prev + curr
        prev = curr
        curr = result
    return result

# A dictionary where each key is n and the corresponding value 
# the is nth Fibonacci number. This is used in fibonacci_dynamic
fib_dict = {0: 0, 1: 1}
def fibonacci_dynamic(n):
    """Return the nth number in the Fibonacci's sequence.
    If n <= 1, return n. If n > 1, return F(n-1) + F(n-2).
    Use dynamic programming.
    """
    if n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        return fib_dict[n]

if __name__ == "__main__":
    """ Test the above functions and compare 
    the time it takes to get the 12th number
    """

    # Recursively find the nth Fib number
    assert fibonacci_recursively(0) == 0
    assert fibonacci_recursively(1) == 1
    assert fibonacci_recursively(2) == 1
    start = timeit.default_timer()
    assert fibonacci_recursively(12) == 144
    print ((timeit.default_timer() - start) * 1000)

    # Iteratively find the nth Fib number
    assert fibonacci_iteratively(0) == 0
    assert fibonacci_iteratively(1) == 1
    assert fibonacci_iteratively(2) == 1
    start = timeit.default_timer()
    assert fibonacci_iteratively(12) == 144
    print ((timeit.default_timer() - start) * 1000)

    # Find the nth Fib number using dynamic programming
    assert fibonacci_dynamic(0) == 0
    assert fibonacci_dynamic(1) == 1
    assert fibonacci_dynamic(2) == 1
    start = timeit.default_timer()
    assert fibonacci_dynamic(12) == 144
    print ((timeit.default_timer() - start) * 1000)