previous = ""

while True:
	sequence = input()
	if sequence == "99999":
		break
	sum = int(sequence[0]) + int(sequence[1])
	direction = ""
	if sum == 0:
		direction = previous
	elif sum % 2 == 0:
		direction = "right"
	elif sum % 2 == 1:
		direction = "left"
	print(direction + " " + sequence[2:])
	previous = direction

