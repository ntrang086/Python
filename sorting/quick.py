"""Implement quick sort.
https://en.wikipedia.org/wiki/Quicksort
"""

def partition_lomuto(array, low, high):
    """Choose a pivot that is the last item in the array.
    Reorder the array so that all items with values less than
    the pivot come before the pivot, while all items with values 
    greater than the pivot come after it. 
    """

    # Pick a pivot
    pivot = array[high]
    # Items low to i are less than or equal to pivot
    i = low
    for j in range(low, high):
        if array[j] < pivot:
            # Swap only if i and j are differnt, i.e. pointing
            # to different items in the array
            if i != j:
                array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i
