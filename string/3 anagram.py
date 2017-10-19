# Check if two strings are anagrams using sorted
def check_anagrams(s1, s2):
	return sorted(s1) == sorted(s2)


# Test the function above
s1 = 'nap'
s2 = 'pan'
s3 = 'abc'

# Return true as s1 and as 2 are anagrams
print (check_anagrams(s1, s2))

# Return false as s1 and s3 are not anagrams
print (check_anagrams(s1, s3))