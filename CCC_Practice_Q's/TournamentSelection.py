


def runFunction():

	v1 = input()
	v2 = input()
	v3 = input()
	v4 = input()
	v5 = input()
	v6 = input()

	wins = 0

	if v1 == "W":
		wins+=1 
	if v2 == "W":
		wins+=1 
	if v3 == "W":
		wins+=1 
	if v4 == "W":
		wins+=1 
	if v5 == "W":
		wins+=1 
	if v6 == "W":
		wins+=1 

	if wins >=5:
		return (1)
	elif wins >= 3:
		return (2)
	elif wins >= 1:
		return (3)
	else:
		return (-1) 


print(runFunction())