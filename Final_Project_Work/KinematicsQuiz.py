import random

x = 0
t = 0
v = random.uniform(0.45,0.45)
a = random.uniform(-0.02,-0.02)
dt = 0.1


print("A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", how long will it take for driver to come to a stop?")
    
answer = float(input("Answer:"))

while v>0:
    v=v+a*dt
    x=x+v*dt
    t=t+dt

if answer != t:
    print("Incorrect. The correct answer is:" + str(t))
else:
    print("Correct")




