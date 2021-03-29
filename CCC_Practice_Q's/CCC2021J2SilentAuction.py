amount = int(input())
names =[]
bids = []

for i in range(0,amount,1):#specifies amount of names and bids there will need to be inputted
	name = input()
	bid = int(input())

	names.append(name)
	bids.append(bid)



highestbid = max(bids)
winner = bids.index(highestbid)
print(names[winner])#since it's a name pair value, this prints name of highest bidder




