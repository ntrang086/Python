"""Given 2 integer arrays, determine if the 2nd array is 
a rotated version of the 1st array. Ex. A = [1, 2, 3, 5, 6, 7, 8]; 
B = [5, 6, 7, 8, 1, 2, 3] is a rotated version of A.
"""

def is_rotated(array_1, array_2):
    """Check if array_2 is a rotated version of array_1"""
    if len(array_1) != len(array_2):
        return False
    if array_1 == array_2:
        return True
    if set(array_1) != set(array_2):
        return False
    index = array_1.index(array_2[0])
    return (array_2 == (array_1[index:] + array_1[:index]))

if __name__ == "__main__":
    # Rotation
    array_1 = [1, 2, 3, 5, 6, 7, 8]
    array_2 = [5, 6, 7, 8, 1, 2, 3]
    assert is_rotated(array_1, array_2)

    # Rotation with repeated numbers
    array_1, array_2 = [1, 2, 3, 5, 6, 7, 8, 1], [5, 6, 7, 8, 1, 1, 2, 3]
    assert is_rotated(array_1, array_2)

    # Different set
    array_1, array_2 = [1, 2, 3, 5, 6, 7, 1], [5, 6, 7, 8, 1, 2, 3]
    assert not is_rotated(array_1, array_2)
    
    # Equal
    array_2 = array_1
    assert is_rotated(array_1, array_2)

    # Empty
    array_1, array_2 = [], []
    assert is_rotated(array_1, array_2)

    # 1 empty, 1 not empty
    array_1, array_2 = [], [1]
    assert not is_rotated(array_1, array_2)
    array_1, array_2 = [1], []
    assert not is_rotated(array_1, array_2)