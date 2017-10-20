# Check if a string is an int or a float
def is_int_or_float(s):
	try:
		if type(int(s)) == int:
			print (s, "is an int")
	except ValueError:
		try:
			if type(float(s)) == float:
				print (s, "is a float")
		except ValueError:
			print (s, "is neither an int or a float")
		

# Test the function above
s1 = '1'
s2 = '1.0'
s3 = 'a'

is_int_or_float(s1)
is_int_or_float(s2)
is_int_or_float(s3)