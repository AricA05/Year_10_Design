import random

score = 0

while True:

    x = 0
    t = 0
    v = round(random.uniform(20,20),2)
    a = round(random.uniform(-0.10,-0.10),2)
    dt = 0.001
    
    
    question = random.choice(["A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", HOW LONG will it take for driver to come to a stop?", "A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", HOW FAR did the driver go until car stopped?"])
    print(question)
    #print("A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", how long will it take for driver to come to a stop?")
        
    answer = float(input("Answer:"))
    
    while v>0:
        v=v+a*dt
        x=x+v*dt
        t=t+dt
    
    if answer != round(t,2) or round(x,2):
        print("Correct. The correct answer is:" + str(round(x,2)))
        #print("Score:",score,"points")
        print("Restart Quiz")
    else:
        print("ok")
        #break
    '''elif answer == round(t,2) OR round(x,2):
        #score += 1
        print("Correct")'''
    #else:
     #   print("ok")
        #print("Score:",score,"points")
    '''elif answer == round(x,2):
        print("correct")
    elif answer != round(x,2):
        print("incorrect")'''

    #else:
        #print("ok")
    '''if answer != round(x,2):
        print("Incorrect")
    elif answer == round(x,2):
        print("Correct")
    else:
        print("ok")'''
