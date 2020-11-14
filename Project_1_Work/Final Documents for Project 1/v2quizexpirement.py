import tkinter as tk 
from tkinter import ttk

def main():

    notebook.add(frame1, text="Question 1")
    notebook.add(frame2, text="Question 2")
    notebook.add(frame3, text="Question 3")
    notebook.add(frame4, text="Question 4")

    tk.Label(frame1, text="Question: How many BicepCurl's per set do you typically do?").grid(row=1, column=3)
    tk.Button(frame1, text="A)10-12", command=add1).grid(row=4, column=2)
    tk.Button(frame1, text="B)15-20", command=add2).grid(row=4, column=3)
    tk.Button(frame1, text="C)21+", command=add3).grid(row=4, column=5)

    tk.Label(frame2, text="Question: How many Planks per set do you typically do?").grid(row=1, column=4)
    tk.Button(frame2, text="A)1-2", command=add1v2).grid(row=4, column=2)
    tk.Button(frame2, text="B)3-4", command=add2v2).grid(row=4, column=4)
    tk.Button(frame2, text="C)5+", command=add3v2).grid(row=4, column=5)

    tk.Label(frame3, text="Question: How many Lunges per set do you typically do?").grid(row=1, column=3)
    tk.Button(frame3, text="A)10-15", command=add1v3).grid(row=4, column=2)
    tk.Button(frame3, text="B)16-20", command=add2v3).grid(row=4, column=3)
    tk.Button(frame3, text="C)21+", command=add3v3).grid(row=4, column=5)


    tk.Label(frame4, text="Question: How many reps per set of your Other exercise do you do?").grid(row=1, column=3)
    tk.Button(frame4, text="A)10-12", command=add1v4).grid(row=4, column=2)
    tk.Button(frame4, text="B)15-20", command=add2v4).grid(row=4, column=3)
    tk.Button(frame4, text="C)21+", command=add3v4).grid(row=4, column=5)

    notebook.pack()

    tk.Label(screen, text="Your Answers:").pack()

    #Label(root, text="Your Answers:").pack()
    #Label(root, textvariable=user_answers).pack()

    #Label(root, text="Total:").pack()
    #Label(root, textvariable=total2).pack()

    #Label(root, text ="Total:").pack()
    #Label(root, textvariable=total3).pack()

#For Question 1:
def add1():
    tk.Label(frame1, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text = "A").pack()
    #user_answers.set(user_answers.get() + "A")
    #counter1()

def add2():
    tk.Label(frame1, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text = "B").pack()
    #user_answers2.set(user_answers2.get() + "B")
    #counter2()

def add3():
    tk.Label(frame1, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()
    #user_answers3.set(user_answers3.get() + "C")
    #counter3()

#For Question 2:
def add1v2():
    tk.Label(frame2, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()
    #user_answers4.set(user_answers4.get() + "A")   
    #counter4()

def add2v2():
    tk.Label(frame2, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()
    #user_answers5.set(user_answers5.get() + "B")
    #counter5()

def add3v2():
    tk.Label(frame2, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()
    #user_answers6.set(user_answers6.get() + "C")
    #counter6()

#For Question 3:
def add1v3():
    tk.Label(frame3, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()
    #user_answers7.set(user_answers7.get() + "A")
    #counter7()

def add2v3():
    tk.Label(frame3, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()
    #user_answers8.set(user_answers8.get() + "B")
    #counter8()

def add3v3():
    tk.Label(frame3, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()
    #user_answers9.set(user_answers9.get() + "C")
    #counter9()

#For Question 4:
def add1v4():
    tk.Label(frame4, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()
    #user_answers10.set(user_answers10.get() + "A")
    #counter10()

def add2v4():
    tk.Label(frame4, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()
    #user_answers11.set(user_answers11.get() + "B")
    #counter11()

def add3v4():
    tk.Label(frame4, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()
    #user_answers12.set(user_answers12.get() + "C")
    #counter12()
    

#For Q#1:
'''def counter1():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers).pack()
    user_answers.set(user_answers.get() + "A")

def counter2():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers2).pack()
    user_answers2.set(user_answers2.get() + "B")

def counter3():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers3).pack()
    user_answers3.set(user_answers3.get() + "C")'''



#For Q#2:
'''def counter4():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers4).pack()
    user_answers4.set(user_answers4.get() + "A")

def counter5():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers5).pack()
    user_answers5.set(user_answers5.get() + "B")

def counter6():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers6).pack()
    user_answers6.set(user_answers6.get() + "C")'''



#For Q#3:
'''def counter7():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers7).pack()
    user_answers7.set(user_answers7.get() + "A")

def counter8():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers8).pack()
    user_answers8.set(user_answers8.get() + "B")

def counter9():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers9).pack()
    user_answers9.set(user_answers9.get() + "C")'''



#For Q#4:
'''def counter10():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers10).pack()
    user_answers10.set(user_answers10.get() + "A")

def counter11():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers11).pack()
    user_answers11.set(user_answers11.get() + "B")

def counter12():
    tk.Label(screen).pack()
    tk.Label(screen, textvariable=user_answers12).pack()
    user_answers12.set(user_answers12.get() + "C")'''


screen = tk.Tk()
screen.title("Progression Quiz")

'''user_answers = tk.StringVar()
user_answers2 = tk.StringVar()
user_answers3 = tk.StringVar()
user_answers4 = tk.StringVar()
user_answers5 = tk.StringVar()
user_answers6 = tk.StringVar()
user_answers7 = tk.StringVar()
user_answers8 = tk.StringVar()
user_answers9 = tk.StringVar()
user_answers10 = tk.StringVar()
user_answers11 = tk.StringVar()
user_answers12 = tk.StringVar()'''



notebook = ttk.Notebook(screen)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)

main()

screen.mainloop()