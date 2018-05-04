"""Find the factorial of a number."""

import math

# A dictionary where each key is a non-negative number
# and the corresponding value is its factorial 
factorial_dict = {0: 1, 1: 1}
def factorial(n):
    """Calculate the factorial of a non-negative integer n"""
    if n in factorial_dict:
        return factorial_dict[n]
    factorial_dict[n] = n * factorial(n - 1)
    return factorial_dict[n]


if __name__ == "__main__":
    assert factorial(2) == 2
    assert factorial(10) == 3628800