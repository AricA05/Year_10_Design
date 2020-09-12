'''isEven tool takes a single integer parameter a>=0 returning true if
a is even and false if a is odd
'''

def isEven(a):
	if a % 2 == 0:
		return True 
#Otherwise:
	return False

#Test code for isEven tool:

print(isEven(0))
print(isEven(10))
print(isEven(9))