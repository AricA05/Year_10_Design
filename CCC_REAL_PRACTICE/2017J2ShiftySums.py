n = int(input())
k = int(input())

total = 0
total += n

for i in range(1,k+1):
	total += n*10**i
print(total)
