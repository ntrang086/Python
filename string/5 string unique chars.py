# Check if a string is composed of all unique characters
def has_unique_chars(s):
	s_dict = {}
	for c in s:
		if c in s_dict:
			return False
		else:
			s_dict[c] = 1
	return True
	

# Test the function above
s1 = 'nap'
s2 = 'naap'

# Return true for s1 and false for s1
print (has_unique_chars(s1))
print (has_unique_chars(s2))