# Check if a string is a palindrome
def is_palindrome(s):
	for i in range(len(s)):
		if s[i] != s[-i-1]:
			return False
	return True

# Find the shortest palindrome in a string
def shortest_palindrome(s):
	palindromes = []
	for i in range(len(s)):
		# Only consider substrings that have at least 3 characters
		for j in range(i+3, len(s)+1):
			print (i, j, s[i:j])
			if is_palindrome(s[i:j]):
				palindromes.append(s[i:j])
	return min(palindromes, key=len)


s = 'abcbaayaa'
print (shortest_palindrome(s))