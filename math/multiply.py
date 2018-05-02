"""Implement a multiply function that multiplies 2 integers without using *."""

def multiply_iteratively(x, y):
    """Multiply two numbers x and y using iteration."""
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    result = 0
    for i in range(abs(y)):
        result += x
    if y > 0:
        return result
    else:
        return -result
    

def multiply_recursively(x, y):
    """Multiply two numbers x and y using recursion."""
    if y == 0:
        return 0
    if y > 0:
        return x + multiply_recursively(x, y - 1)
    if y < 0:
        return -multiply_recursively(x, -y)


if __name__ == "__main__":
    assert multiply_iteratively(1, 2) == 2
    assert multiply_iteratively(5, 6) == 30
    assert multiply_iteratively(-5, -6) == 30
    assert multiply_iteratively(5, -6) == -30

    assert multiply_recursively(1, 2) == 2
    assert multiply_recursively(5, 6) == 30
    assert multiply_recursively(-5, -6) == 30
    assert multiply_recursively(5, -6) == -30