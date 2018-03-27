"""Implement quick sort.
https://en.wikipedia.org/wiki/Quicksort
"""

def quick_sort_lomuto(array, low, high):
    """Divide a large array into two smaller sub-arrays: the low 
    items and the high items; then recursively sort the sub-arrays.
    """

    # Base case: a list with 1 or 0 item is sorted
    if len(array) <= 1:
        return array
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


if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print (quick_sort_lomuto(array, 0, len(array) - 1))