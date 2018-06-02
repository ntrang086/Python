"""Given two Integers N and M, and print all the terms of the series upto
M-terms of the N-bonacci Numbers. For example, when N = 2, the sequence
becomes Fibonacci, when n = 3, sequence becomes Tribonacci.

In general, in N-bonacci sequence, we use sum of preceding N numbers from the
next term. For example, a 3-bonacci sequence is the following:
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81

The Fibonacci sequence is a set of numbers that starts with one or zero, 
followed by a one, and proceeds based on the rule that each number is equal
to the sum of preceding two numbers 0, 1, 1, 2, 3, 5, 8…

Examples:
Input: N = 3, M = 8
Output: 0, 0, 1, 1, 2, 4, 7, 13

Input: N = 4, M = 10
Output: 0, 0, 0, 1, 1, 2, 4, 8, 15, 29
"""

def n_bonacci(n, m):
    # Initialize the first (n - 1) terms with 0, and the next 2 terms with 1
    results = [0] * (n - 1)
    results.append(1)
    results.append(1)
    if m <= n:
        return results[: m]
    for i in range(n + 1, m):
        results.append(results[i - 1] * 2 - results[ - (n + 1)])
    return results


if __name__ == "__main__":
    assert n_bonacci(3, 8) == [0, 0, 1, 1, 2, 4, 7, 13]
    assert n_bonacci(4, 10) == [0, 0, 0, 1, 1, 2, 4, 8, 15, 29]
    assert n_bonacci(5, 15) == [0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464]