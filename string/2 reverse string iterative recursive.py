def reverse_string_iteratively(s):
	i = 1
	reverse_s = ""
	while i <= len(s):
		reverse_s += s[-i]
		i += 1
	return reverse_s


def reverse_string_recursively(s):
	if s == "":
		return s
	else:
		return reverse_string_recursively(s[1:]) + s[0]

s = 'abcdfg'
print (reverse_string_iteratively(s))
print (reverse_string_recursively(s))