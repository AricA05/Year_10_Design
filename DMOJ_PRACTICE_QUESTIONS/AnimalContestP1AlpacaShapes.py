S, R = map(int, input().split())

AreaofSquare = S*S
AreaofCirlce = 3.14*(R*R)

if AreaofSquare>AreaofCirlce:
	print("SQUARE")
else:
	print("CIRCLE")