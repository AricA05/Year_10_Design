L = int(input())
message = []

for i in range(L):
	msg = input().split()
	message.append(msg)

for i in message:
	print(i[1] * int(i[0]))
