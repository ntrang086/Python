def reverse_string_iteratively(s):
	i = 1
	reverse_s = ""
	while i <= len(s):
		reverse_s += s[-i]
		i += 1
	return reverse_s


def reverse_string_recursively(s):
	i = 1
	reverse_s = ""
	while i <= len(s):
		reverse_s += s[-i]
		i += 1
	return reverse_s

s = 'aabbccdeeffghh'
print (reverse_string_iteratively(s))
print (reverse_string_recursively(s))