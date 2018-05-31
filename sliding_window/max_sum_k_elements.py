"""Given an array of integers of size ‘n’, calculate the maximum sum of ‘k’ 
consecutive elements in the array.
"""

def max_sum(array, k):
    if len(array) < k:
        return None
    if len(array) == k:
        return sum(array)
    max_sum = sum(array[:k])
    for i in range(1, len(array) - k + 1):
        current_sum = max_sum - array[i - 1] + array[i + k - 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

if __name__ == "__main__":
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    assert max_sum(arr, 4) == 39 # Adding subarray [4, 2, 10, 23]
    assert max_sum([100, 200, 300, 400], 2) == 700
    assert max_sum([2, 3], 2) == 5
    assert max_sum([2, 3], 3) == None

