"""You are given n activities with their start and finish times. Select the 
maximum number of activities that can be performed by a single person, 
assuming that a person can only work on a single activity at a time.
We will use quick sort to sort arrays according to finishing times.
"""

def select_activities(start_times, finish_times):
    # Sort the arrays using quick sort
    finish_times, start_times = quick_sort_hoare(finish_times, start_times, 0, len(finish_times) - 1)

    selected_i = []
    for i in range(len(finish_times)):
        # Select the first activity from the sorted array
        if i == 0:
            selected_i.append(i)
        # For the rest, the start time of an activity is >= the finish time of
        # previously selected activity then select this activity
        else:
            if start_times[i] >= finish_times[len(selected_i) - 1]:
                selected_i.append(i)
    return selected_i

def quick_sort_hoare(array_1, array_2, low, high):
    """Perform quick sort according to array_1."""

    if low < high:
        p = partition_hoare(array_1, array_2, low, high)
        quick_sort_hoare(array_1, array_2, low, p)
        quick_sort_hoare(array_1, array_2, p + 1, high)
    return array_1, array_2

def partition_hoare(array_1, array_2, low, high):
    """Use two indices i and j that start at the ends of the array,
    then move toward each other, until they detect an inversion: 
    a pair of items, one greater than or equal to the pivot, one 
    lesser or equal, that are in the wrong order relative to each 
    other. The inverted items are then swapped. When the indices
    meet, return the final index.
    """

    # Pick a pivot
    pivot = array_1[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array_1[i] < pivot:
            i += 1
        j -= 1
        while array_1[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array_1[i], array_1[j] = array_1[j], array_1[i]
        array_2[i], array_2[j] = array_2[j], array_2[i]


if __name__ == "__main__":
    # Sorted arrays of start and finish times
    sorted_s = [1, 3, 0, 5, 5, 8]
    sorted_f = [2, 4, 6, 7, 9, 9]
    assert select_activities(sorted_s, sorted_f) == [0, 1, 3, 4]
    
    # Unsorted arrays of start and finish times
    unsorted_s = [5, 3, 1, 0, 5, 8]
    unsorted_f = [9, 4, 2, 6, 7, 9]
    assert (select_activities(unsorted_s, unsorted_f))  == [0, 1, 3, 4]