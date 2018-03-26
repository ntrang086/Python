"""Implement merge sort."""

def merge_sort_top_down(array):
    """Recursively divide the input list into smaller sublists 
    until the sublists are trivially sorted, and then merge
    the sublists while returning up the call chain.
    https://en.wikipedia.org/wiki/Merge_sort"""
    
    # Base case: a list with 1 or 0 item is sorted
    if len(array) <= 1:
        return array
    
    # Split the list into sublists
    left = []
    right = []
    for i in range(len(array)):
        if i < len(array)/2:
            left.append(array[i])
        else:
            right.append(array[i])
    
    # Recursively sort both sublists
    left = merge_sort_top_down(left)
    right = merge_sort_top_down(right)

    # Merge the now-sorted sublists
    return merge(left, right)

def merge(left, right):
    """Helper function for merge_sort_top_down. 
    Merge left and right sublists."""

    # Compare
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    # If either left or right has items left, 
    # add them to result
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result


if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print (merge_sort_top_down(array))    