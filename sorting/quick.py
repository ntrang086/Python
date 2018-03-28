"""Implement quick sort.
https://en.wikipedia.org/wiki/Quicksort
"""

def quick_sort_lomuto(array, low, high):
    """Divide a large array into two smaller sub-arrays: the low 
    items and the high items; then recursively sort the sub-arrays.
    """

    if low < high:
        p = partition_lomuto(array, low, high)
        quick_sort_lomuto(array, low, p - 1)
        quick_sort_lomuto(array, p + 1, high)
    return array

def partition_lomuto(array, low, high):
    """Choose a pivot that is the last item in the array.
    Reorder the array so that all items with values less than
    the pivot come before the pivot, while all items with values 
    greater than the pivot come after it. 
    Return the index of pivot from the reordered array.
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

def quick_sort_hoare(array, low, high):
    """Divide a large array into two smaller sub-arrays: the low 
    items and the high items; then recursively sort the sub-arrays.
    """

    if low < high:
        p = partition_hoare(array, low, high)
        quick_sort_hoare(array, low, p - 1)
        quick_sort_hoare(array, p + 1, high)
    return array

def partition_hoare(array, low, high):
    """Use two indices i and j that start at the ends of the array,
    then move toward each other, until they detect an inversion: 
    a pair of items, one greater than or equal to the pivot, one 
    lesser or equal, that are in the wrong order relative to each 
    other. The inverted items are then swapped. When the indices
    meet, return the final index.
    """

    # Pick a pivot
    pivot = array[low]
    i = low
    j = high
    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print (quick_sort_lomuto(array, 0, len(array) - 1))
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print (quick_sort_hoare(array, 0, len(array) - 1))