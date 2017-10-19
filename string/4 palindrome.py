def reverse_string_iteratively(s):
	i = 1
	reverse_s = ""
	while i <= len(s):
		reverse_s += s[-i]
		i += 1
	return reverse_s


def is_palindrome(s):
	return s == reverse_string_iteratively(s)

s1 = 'madam'
s2 = 'abc'
print (is_palindrome(s1))
print (is_palindrome(s2))