"""Implement binary search in a sorted array of integers."""

def binary_search(array, left, right, key):
    """Search for key in a sorted array of integers.
    Return index of the key in array if found; otherwise return -1.
    """
    if right >= left:
        mid = int(left + (right - left) / 2)
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return binary_search(array, left, mid - 1, key)
        else:
            return binary_search(array, mid + 1, right, key)
    return -1
 

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 17]
    assert binary_search(array, 0, len(array) - 1, 8) == 7
    assert binary_search(array, 0, len(array) - 1, 10) == -1