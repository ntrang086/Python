"""Find the most common and the least common integer in an array.
"""

def count_integers(array):
    """Store integers and their counts as key-value pairs in a dictionary.
    """
    freq_dict = {}
    for i in array:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    return freq_dict

def least_common_integer(array):
    """Find the least common integer in an array.
    """
    freq_dict = count_integers(array)
    min_count = len(array)
    least_common_int = -1
    for integer in freq_dict:
        count = freq_dict[integer]
        # Use >= instead of > to make sure that least_common_int
        # is not -1 in case the array has only 1 unique item.
        if min_count >= count:
            min_count = count
            least_common_int = integer
    return least_common_int

def most_common_integer(array):
    """Find the most common integer in an array.
    """
    freq_dict = count_integers(array)
    max_count = 0
    most_common_int = -1
    for integer in freq_dict:
        count = freq_dict[integer]
        if max_count < count:
            max_count = count
            most_common_int = integer
    return most_common_int

if __name__ == "__main__":
    array = [2, 2, 3, 3, 3, 1]
    print (least_common_integer(array))
    print (most_common_integer(array))