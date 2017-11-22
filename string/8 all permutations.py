def find_all_permutations(s):
	if s == '':
		return ['']
	previous_list = find_all_permutations(s[1:len(s)])
	permutations = []
	for i in range(len(previous_list)):
		for j in range(len(s)):
			new_permutation = previous_list[i][0:j] + s[0] + previous_list[i][j:len(s)-1]
			if new_permutation not in permutations:
				permutations.append(new_permutation)
	return permutations

s = 'abc'
print (find_all_permutations(s))