#Problem: https://www.nayuki.io/res/dwite-programming-contest-solutions/dwite-200410-p2.pdf


#this only works with decimals, not colon signs
'''def conversion():
	t = 17.12

	if 0 <= t < 12:
		print(t, "AM")

	if 12 <= t < 24:
		print(t-12, "PM") 

conversion()'''



#Solution 1
'''time = "18:12"
XM = str

hour = int(time[:2])
minute = (time[-2:])

hour2 = (hour - 12)

if 0 <= hour < 12:
	print(hour,":",minute, "AM")

if 12 <= hour < 24:
	print(hour2,":",minute, "PM")'''



#Solution 2

currentTime = "00:00"

h = int(currentTime[:2])

m = (currentTime[-2:])

timeOfDay = "AM"


if 12 <= h <= 23:
	timeOfDay = "PM";
	h = h - 12
if (h==0):
	h=12
print(str(h)+":"+m+" "+timeOfDay)
