"""Implement a square root function."""

def square_root_babylonian(n):
    """Calculate the square root of n using Babylonian method
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    """
    if n < 0:
        return None
    if n <= 1:
        return n
    sol = n / 2
    updated_sol = n / sol
    e = 0.000001
    while sol - updated_sol > e:
        sol = (sol + updated_sol) / 2
        updated_sol = n / sol
    return sol
    
if __name__ == "__main__":
    print (square_root_babylonian(20))
    print (square_root_babylonian(100))