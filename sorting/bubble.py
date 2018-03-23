"""Implement bubble sort. Sort an array in an ascending order"""

def bubble_sort(array):
    """Repeatedly swap the adjacent elements of an array 
    if they are in wrong order."""

    # Keep track of whether a swap happened in a pass through array
    swapped = True
    # Number of swaps done in a pass; initialized with 
    # the worst case value which is len(array) - 1
    num_swaps = len(array) - 1
    while swapped:
        swapped = False
        for i in range(num_swaps):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # The last swapped item in the above for loop is in a correct 
        # position so we don't need to check it again in the next pass
        num_swaps -= 1
    return array


if __name__ == "__main__":
    array = [10, 2, 3, 6, 20]
    print (bubble_sort(array))