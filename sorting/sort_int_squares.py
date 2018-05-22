"""Given: sorted array of integers.
Return: sorted array of squares of those integers.
Integers can be negative.
Ex: [-1,3,5] -> [1,9,25] 
"""

def squares_of_integers(array):
    """O(nlogn) solution. Python's built-in function sorted uses 
    Timsort which is (nlogn).
    https://en.wikipedia.org/wiki/Timsort.
    """
    abs_array = [abs(n) for n in array]
    abs_array = sorted(abs_array)
    squares = [n ** 2 for n in abs_array]
    return squares    

def squares_of_integers_2(array):
    """O(n) solution."""
    s = 0
    e = len(array) - 1
    squares = []
    while (s <= e):
        squared_s = array[s] ** 2
        squared_e = array[e] ** 2
        if squared_s >= squared_e:
            squares.append(squared_s)
            s += 1
        else:
            squares.append(squared_e)
            e -= 1
    return list(reversed(squares))


if __name__ == "__main__":
    array = [-5, -4, -2, 0, 2, 5]
    assert squares_of_integers(array) == [0, 4, 4, 16, 25, 25]
    assert squares_of_integers_2(array) == [0, 4, 4, 16, 25, 25]

    array_2 = [-1, 0, 2, 5]
    assert squares_of_integers_2(array_2) == squares_of_integers(array_2) 

    array_3 = [-7, -6,-1, 0, 1, 5]
    assert squares_of_integers_2(array_3) == squares_of_integers(array_3)