
N = int(input())
weights = input()#weight numbers for emeralds
l = list(map(int,weights.split(' ')))#converts inputs to an array

answer = 0
ctr = 0

for i in range(len(l)):
    if (l[i] % 2 == 0):
        ctr += l[i]#addition assignment operator!
        answer = max(answer, ctr)
    else:
        ctr = 0
print(answer)
