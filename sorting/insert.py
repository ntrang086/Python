"""Implement insertion sort."""

def insertion_sort(array):
    """Insertion sort iterates, consuming one input element each repetition, 
    and growing a sorted output list. At each iteration, insertion sort 
    removes one element from the input data, finds the location it belongs 
    within the sorted list, and inserts it there. It repeats until no 
    input elements remain.
    https://en.wikipedia.org/wiki/Insertion_sort"""

    # Move the left boundary of the unsorted sublist one at a time
    for i in range(1, len(array)):
        current_item = array[i]
        j = i
        # Shift right items in the sorted sublist array[0:j] that are  
        # greater than current_item, starting from the rightmost.        
        while j > 0 and array[j - 1] > current_item:
            array[j] = array[j - 1]
            j -= 1
        # Insert current_item into the correct location in the sorted array
        array[j] = current_item
    return array


if __name__ == "__main__":
    array = [10, 6, 2, 3, 9]
    print (insertion_sort(array))