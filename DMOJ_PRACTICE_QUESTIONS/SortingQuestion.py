n = int(input())
array = []

for i in range(0,n,1):
	nums = int(input())
	array.append(nums)

array.sort()

print(*array, sep ="\n")
