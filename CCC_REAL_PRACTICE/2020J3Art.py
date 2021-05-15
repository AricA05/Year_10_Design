N = int(input())

X, Y = [], []

for i in range(0,N,1):
	Xp, Yp = input().split(",")
	X.append(int(Xp))
	Y.append(int(Yp))


MAXx = (max(X))
MAXy = (max(Y))

MINx = (min(X))
MINy = (min(Y))


FinalBottomLeftX = MINx - 1
FinalBottomLeftY = MINy - 1

FinalTopRightX = MAXx + 1
FinalTopRightY = MAXy + 1

print(str(FinalBottomLeftX)+","+str(FinalBottomLeftY))
print(str(FinalTopRightX)+","+str(FinalTopRightY))

