N = int(input())
b1 = input()
b2 = input()


ctr = 0

for i in range(len(b1)):
	if b1[i] == "0" and b2[i] == "0":
		ctr += 1
print(ctr)