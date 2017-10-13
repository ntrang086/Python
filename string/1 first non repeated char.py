def first_non_repeated_char(s):
	from collections import OrderedDict
	count_repeated_char = OrderedDict([])
	for char in s:
		if char in count_repeated_char:
			count_repeated_char[char] += 1
		else:
			count_repeated_char[char] = 1
	for char in count_repeated_char:
		if count_repeated_char[char] == 1:
			return char


s = 'aabbccdeeffghh'
print (first_non_repeated_char(s))