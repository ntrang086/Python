"""Given an array of n integers, for each element, print the distance
to the closest zero. Array has a minimum of 1 zero in it.
"""

def distance_to_closest_0(array):
    distances = [0] * len(array)
    # If the first element is 0, the distance will be 0
    if array[0] == 0:
        distances[0] = 0
    # Otherwise initialize with a maximum value
    else:
        distances[0] = len(array) - 1
    for i in range(1, len(array)):
        if array[i] == 0:
            distances[i] = 0
        else:
            distances[i] = distances[i - 1] + 1
    # Traverse from right to left and store the minimum
    # of distance if found from right to left or left to right
    j = len(array) - 2
    while j >= 0:
        if array[j] == 0:
            distances[j] = 0
        else:
            distances[j] = min(distances[j], distances[j + 1] + 1)
        j -= 1
    return distances

if __name__ == "__main__":
    array = [2, 1, 0, 3, 0, 0, 3, 2, 4]
    assert distance_to_closest_0(array) == [2, 1, 0, 1, 0, 0, 1, 2, 3]
