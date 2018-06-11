"""Find the integer that occurs only once in an array
where other integers repeat three times.
"""
def find_only_occurrence(array):
    # Add up all integers in the array
	sum_array = sum(array)
    # Create a set of integers from array and add up all items
	sum_set = sum(set(array))
    # Multiply the sum_set by 3, substract the above sum_array 
    # from this multiplication result, and divide the difference by 2
	return int((sum_set * 3 - sum_array) / 2)

if __name__ == "__main__":
	array = [1, 4, 2, 1, 2, 3, 1, 2, 3, 3]
	# Should return 4
	print(find_only_occurrence(array))