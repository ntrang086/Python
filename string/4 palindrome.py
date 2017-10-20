def reverse_string_iteratively(s):
	i = 1
	reverse_s = ""
	while i <= len(s):
		reverse_s += s[-i]
		i += 1
	return reverse_s

# Check if a string is a palindrome using reverse_string_iteratively function
def is_palindrome(s):
	return s == reverse_string_iteratively(s)

# Another function to check if a string is a palindrome without using reverse_string_iteratively function
def is_palindrome2(s):
	for i in range(len(s)):
		if s[i] != s[-i-1]:
			return False
	return True

s1 = 'madam'
s2 = 'abc'
print (is_palindrome(s1))
print (is_palindrome(s2))
print (is_palindrome2(s1))
print (is_palindrome2(s2))