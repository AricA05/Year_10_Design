N = int(input())

area = 0

h = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(N):
	area += (h[i] + h[i + 1])/2 * w[i]
print(area)

