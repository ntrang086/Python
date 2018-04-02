"""Count pairs in an integer array whose sum is equal to a given number 
- do it in linear time
"""

def count_pairs(array, total):
    int_set = set(array)
    count = 0
    for i in range(len(array)):
        if (total - array[i]) in int_set:
            count += 1
        # Exclude the pair (array[i], array[i])
        if (total - array[i] == array[i]):
            count -= 1
    return count / 2

if __name__ == "__main__":
    array = [1, 7, 5, -1]
    print (count_pairs(array, 6))
    