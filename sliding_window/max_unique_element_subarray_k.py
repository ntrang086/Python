"""Given an array and an integer k, find the maximum unique element 
of every segment of length k.

Examples:
Input : a = [1, 2, 2, 3, 3], k = 3.
Output : [1, 3, 2]
For segment (1, 2, 2), Maximum = 1.
For segment (2, 2, 3), Maximum = 3.
For segment (2, 3, 3), Maximum = 2. 

Input : a = [3, 3, 3, 4, 4, 2], k = 4.
Output : [4, None, 3]
Observation: There are len(a) - k + 1 subarrays to evaluate.
"""
from sortedcontainers import SortedSet
def max_unique_element(array, k):
    """We need 2 data structures will update as we move the sliding window.:
    - A sorted set to keep track of seen items that are unique in each subarray
    - A dictionary to keep track of count for each item in each subarray
    We will return a list of max elements for subarrays
    """
    max_elements = []
    unique_seen = SortedSet()
    counts = dict()
    # Find the max unique value for the first subarray
    for e in array[: k]:
        if e not in counts:
            counts[e] = 1
            unique_seen.add(e)
        else:
            counts[e] += 1
            unique_seen.discard(e)
    if len(unique_seen) > 0:
        # Since unique_seen is a sorted set, the last item is the largest one
        max_elements.append(unique_seen[-1])
    else:
        max_elements.append(None)            
    for i in range(1, len(array) - k + 1):
        # Update counts and unique_seen for the last item of previous subarray
        counts[array[i - 1]] -= 1
        if counts[array[i - 1]] == 1:
            unique_seen.add(array[i - 1])
        else:
            unique_seen.discard(array[i - 1])

        # Update counts and unique_seen for the new member of current subarray
        if array[i + k - 1] not in counts or counts[array[i + k -1]] == 0:
            counts[array[i + k - 1]] = 1
            unique_seen.add(array[i + k - 1])
        else:
            counts[array[i + k - 1]] += 1
            unique_seen.discard(array[i + k - 1])
        # Recoard the max unique element for the current subarray, if any
        if len(unique_seen) > 0:
            max_elements.append(unique_seen[-1])
        else:
            max_elements.append(None)
    return max_elements


if __name__ == "__main__":
    array = [1, 2, 2, 3, 3]
    assert max_unique_element(array, 3) == [1, 3, 2]
    array = [1, 2, 2, 1, 3, 3]
    assert max_unique_element(array, 3) == [1, 1, 3, 1]
    array = [3, 3, 3, 4, 4, 2]
    assert max_unique_element(array, 4) == [4, None, 3]