"""Find the common elements of 2 int arrays.
"""
def common_ints(array_1, array_2):
    return set(array_1).intersection(set(array_2))

if __name__ == "__main__":
    array_1 = [1, 4, 2, 3, 3]
    array_2 = [5, 4, 6, 3, 3]
    # Should return 3 and 4
    print (common_ints(array_1, array_2))