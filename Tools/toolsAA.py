#Tool 1: isEven tool, this tool determines if a number is odd or even.
#If number is even, it returns true, odd is false
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



#Tool 2: missing char tool 
def missing_char(str, n):
  
  newStr = ""
  newStr = str[0:n] + str[n + 1: len(str)]
  return newStr

'''
How this was solved layout:
012345    missing_char ("kitten",1) --> ktten    str[0:1] + str[2:6]
kitten    missing_char ("kitten",4) --> kittn    str[0:4] + str[5:6]

Now, Generalize the two examples to get a solution:

str[0:n] + str[n + 1: len(str)]

Notes:
- len(str) means length of string. The string is the word, so in this case
it is kitten
- missing_char means missing character (letter)
- n is the missing character 
'''