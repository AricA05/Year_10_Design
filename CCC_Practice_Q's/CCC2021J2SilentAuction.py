amount = int(input())
names =[]
bids = []

for i in range(0,amount,1):
	name = input()
	bid = int(input())

	names.append(name)
	bids.append(bid)



highestbid = max(bids)
winner = bids.index(highestbid)
print(names[winner])




