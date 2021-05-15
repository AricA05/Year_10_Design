
word = input()

Success = True

for i in range(len(word)):
	if word[i] == "I" or word[i] == "O" or word[i] == "S" or word[i] == "H" or word[i] == "Z" or word[i] == "X" or word[i] == "N":
		Success = True
	else:
		print("NO")
		Success = False
		break
if Success == True:
	print("YES")

