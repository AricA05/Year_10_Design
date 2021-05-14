#sequence of 5 digits representing a direction to turn and the number of step to take
#first two digits represent the direction to turn: sum is odd = left, sum is even and not zero = right, sum is zero = turn same as previous
#remaining three digits represent number of steps to take which will always be at least 100


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

