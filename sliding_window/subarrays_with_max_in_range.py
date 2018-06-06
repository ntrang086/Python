"""Given an array of N elements and L and R, count the number of subarrays 
whose max. element is >= L, <= R. Examples:
Input : array = [2, 0, 11, 3, 0]
          L = 1, R = 10
Output : 4. the sub-arrays are [2], [2, 0], [3], [3, 0]

Input : array = [3, 4, 1]
          L = 2, R = 4 
Output : 5. the sub-arrays are [3], [4], [3, 4], [4, 1], [3, 4, 1]
Observations:
- Elements > R are never inc in any subarray.
- Elements < L can be inc in subarray as long as there is min. 1 element
between L and R inclusive.
- The number of all possible subarrays of an array of size N is N * (N + 1)/2. 
This is based on the sum of sequences 1 + 2 + 3 + ... + n = n x (n + 1) / 2
"""
from copy import deepcopy

def count_subarrays(n):
    """Helper function to count the number of subarrays formed by n elements"""
    return int(n * (n + 1) / 2)

def subarrays_max_in_range(array, l, r):
    """We keep track of two counts for each subarray:
    - inc: count of all elements <= R
    - exc: count of all elements < L
    The count for a subarray is count_subarrays(inc) - count_subarrays(exc)
    """
    inc = 0
    exc = 0
    result = 0
    for i in range(len(array)):
        # If an element > r, we get the count for the previous subarray
        # and reset inc and exc
        if array[i] > r:
            result += count_subarrays(inc) - count_subarrays(exc)
            inc = 0
            exc = 0
        # If an element is within the defined range, we increment inc
        elif array[i] <= r and array[i] >= l:
            result -= count_subarrays(exc)
            exc = 0
            inc += 1
        # If an element is < l, then we increment two counts
        else:
            inc += 1
            exc += 1
    result += count_subarrays(inc) - count_subarrays(exc)
    return result

if __name__ == "__main__":
    assert subarrays_max_in_range([2, 0, 11, 3, 0], 1, 10) == 4
    assert subarrays_max_in_range([3, 4, 1], 2, 4) == 5
    assert subarrays_max_in_range([0, 1, 2, 1], 2, 4) == 6
    