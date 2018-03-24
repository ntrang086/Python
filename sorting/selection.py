"""Implement selection sort."""

def selection_sort(array):
    """Divide the input list into two parts: the sublist of items 
    already sorted, which is built up from left to right at the front (left) 
    of the list, and the sublist of items remaining to be sorted that occupy 
    the rest of the list. Initially, the sorted sublist is empty and the 
    unsorted sublist is the entire input list. The algorithm proceeds by 
    finding the smallest (or largest, depending on sorting order) element 
    in the unsorted sublist, exchanging (swapping) it with the leftmost 
    unsorted element (putting it in sorted order), and moving the sublist 
    boundaries one element to the right.
    https://en.wikipedia.org/wiki/Selection_sort"""

    # Move the left boundary of the unsorted sublist one at a time
    for i in range(len(array) - 1):
        # Find the index of the min item in the unsorted part of array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the min item with the leftmost item of the unsorted part
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    array = [10, 6, 2, 3, 9]
    print (selection_sort(array))