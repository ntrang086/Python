"""Implement binary search in a sorted array of integers
that has been rotated an unknown number of times.
"""

def binary_search_rotated(array, left, right, key):
    """Search for key in a sorted array of integers
    that has been rotated an unknown number of times.
    Return index of the key in array if found; otherwise return -1.
    """
    if right >= left:
        mid = int(left + (right - left) / 2)
        if array[mid] == key:
            return mid
        # If array[left : mid] is sorted
        elif array[left] <= array[mid]:
            print ("[left:mid] is sorted")
            # If key is in array[left:mid]
            if key >= array[left] and key < array[mid]:
                return binary_search_rotated(array, left, mid - 1, key)
            else:
                return binary_search_rotated(array, mid + 1, right, key)
        # If array[mid + 1 : right] is sorted
        else:
            # If key is in array[mid + 1 : right]
            if key > array[mid] and key <= array[right]:
                return binary_search_rotated(array, mid + 1, right, key)
            else:
                return binary_search_rotated(array, left, mid - 1, key)
    return -1
 

if __name__ == "__main__":
    array = [15, 16, 19, 20, 25, 1, 3, 4]
    assert binary_search_rotated(array, 0, len(array) - 1, 4) == 7
    assert binary_search_rotated(array, 0, len(array) - 1, 15) == 0
    assert binary_search_rotated(array, 0, len(array) - 1, 25) == 4
    