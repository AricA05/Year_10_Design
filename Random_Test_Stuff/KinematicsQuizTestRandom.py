import random

score = 0

while True:

    x = 0
    t = 0
    v = round(random.uniform(3,112),2)
    a = round(random.uniform(-0.10,-4.25),2)
    dt = 0.001
    
    
    question1 = "A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", HOW LONG will it take for driver to come to a stop?"
    question2 = "A driver is travelling East with a velocity (m/s) of " + str(v) + ", the driver is braking with an acceleration of " + str(a) + ", HOW FAR will the driver go until stop?"


    GivenQuestion = random.choice([question1, question2])
    print(GivenQuestion)
    
    def QuestionNum1():
        answer = float(input("Answer:"))

        global x
        global t
        global v
        global a
        global dt
        global score

        while v>0:
            TA = -v/a
        
            if answer != round(TA,2):
                print("Incorrect. The correct answer is:" + str(round(TA,2)))
                print("Score:",score,"points")
                print("Restart Quiz")
                break
            else:
                score += 1
                print("Correct")
                print("Score:",score,"points")
                break

    def QuestionNum2():
        answer = float(input("Answer:"))

        global x
        global t
        global v
        global a
        global dt
        global score

        while v>0:
            V2 = v*v
            A2 = 2*a
            XA = -V2/A2
        
            if answer != round(XA,2):
                print("Incorrect. The correct answer is:" + str(round(XA,2)))
                print("Score:",score,"points")
                print("Restart Quiz")
                break
            else:
                score += 1
                print("Correct")
                print("Score:",score,"points")
                break



    if GivenQuestion == question1:
        QuestionNum1()
    else:
        QuestionNum2()

