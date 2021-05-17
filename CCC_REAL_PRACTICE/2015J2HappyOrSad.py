sentence = input()

x = ":-)"
countHappy = sentence.count(x)

y = ":-("
countSad = sentence.count(y)

if countHappy > countSad:
	print("happy")
elif countSad > countHappy:
	print("sad")
elif countHappy == 0 and countSad == 0:
	print("none")
else:
	print("unsure")
