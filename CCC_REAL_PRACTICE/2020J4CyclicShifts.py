T = input("")
S = input("")
ans = False

for i in range(len(S)):
    if S in T:
        ans = True
    else:
        S = S[1:] + S[0]

if ans:
    print("yes")
else:
    print("no")