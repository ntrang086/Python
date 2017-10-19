# Check if two strings are anagrams using sorted
def check_anagrams(s1, s2):
	return sorted(s1) == sorted(s2)

# Check if two strings are anagrams using Counter
def check_anagrams2(s1, s2):
	from collections import Counter
	return Counter(s1) == Counter(s2)

# Check if two strings are anagrams by comparing the number of occurrences of each charater in two strings
def check_anagrams3(s1, s2):
	s1_dict = {}
	for c in s1:
		if c in s1_dict:
			s1_dict[c] += 1
		else:
			s1_dict[c] = 1
	
	s2_dict = {}
	for c in s2:
		if c in s2_dict:
			s2_dict[c] += 1
		else:
			s2_dict[c] = 1
	return s1_dict == s2_dict


# Test the functions above
s1 = 'nap'
s2 = 'pan'
s3 = 'abc'

# Return true as s1 and as 2 are anagrams
print (check_anagrams(s1, s2))
print (check_anagrams2(s1, s2))
print (check_anagrams3(s1, s2))

# Return false as s1 and s3 are not anagrams
print (check_anagrams(s1, s3))
print (check_anagrams2(s1, s3))
print (check_anagrams3(s1, s3))