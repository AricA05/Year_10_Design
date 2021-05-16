N = int(input())
day1 = input()
day2= input()

ctr = 0

for i in range(0,N):
	if day1[i] == day2[i] == "C":
		ctr += 1
print(ctr)
