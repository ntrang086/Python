"""Given a Fibonacci number, find which index it occurs at."""

import math

def fibonacci_index(fib_num):
    """Use iteration to find the index of fib_num."""
    if fib_num <= 1:
        return fib_num
    index = 1
    prev = 0
    curr = 1
    result = 1
    while result < fib_num:
        index += 1
        result = prev + curr
        prev = curr
        curr = result
    return index

def fibonacci_index_formula(fib_num):
    """Use a formula https://en.wikipedia.org/wiki/Fibonacci_number.
    """
    phi = (1 + math.sqrt(5)) / 2
    return round(math.log(fib_num * math.sqrt(5), phi))

if __name__ == "__main__":
    # Find the index of a Fibonacci number using iteration
    assert fibonacci_index(0) == 0
    assert fibonacci_index(1) == 1
    assert fibonacci_index(144) == 12

    # Find the index of a Fibonacci number using a formula
    assert fibonacci_index_formula(1) == 2
    assert fibonacci_index_formula(2) == 3
    assert fibonacci_index_formula(144) == 12