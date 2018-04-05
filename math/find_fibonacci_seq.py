"""Generate a Fibonacci sequence with an input n."""

def fibonacci_seq_iteratively(n):
    """Return a Fibonacci sequence with n numbers.
    Use iteration.
    """
    if n <= 1:
        return [i for i in range(n + 1)]
    prev = 0
    curr = 1
    result = 1
    fib_seq = [prev, curr]
    for i in range(2, n + 1):
        result = prev + curr
        fib_seq.append(result)
        prev = curr
        curr = result
    return fib_seq

if __name__ == "__main__":   
    assert fibonacci_seq_iteratively(0) == [0]
    assert fibonacci_seq_iteratively(1) == [0, 1]
    assert fibonacci_seq_iteratively(2) == [0, 1, 1]
    assert fibonacci_seq_iteratively(12) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]