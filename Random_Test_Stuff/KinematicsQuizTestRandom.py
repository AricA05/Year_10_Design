import random

score = 0

while True:

    x = 0
    t = 0
    v = round(random.uniform(3,112),2)
    a = round(random.uniform(-0.10,-4.25),2)
    dt = 0.001
    
    
    print("A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", how long will it take for driver to come to a stop?")
        
    answer = float(input("Answer:"))
    
    while v>0:
        v=v+a*dt
        x=x+v*dt
        t=t+dt
    
    if answer != round(t,2):
        print("Incorrect. The correct answer is:" + str(round(t,2)))
        print("Score:",score,"points")
        print("Restart Quiz")
        break
    else:
        score += 1
        print("Correct")
        print("Score:",score,"points")
        
