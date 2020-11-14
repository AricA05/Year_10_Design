from tkinter import *
from tkinter import ttk

def main():

    notebook.add(frame1, text="Question 1")
    notebook.add(frame2, text="Question 2")
    notebook.add(frame3, text="Question 3")
    notebook.add(frame4, text="Question 4")

    Label(frame1, text="Question: How many Push-Up's per Set do you typically do?").grid(row=1, column=3)
    Button(frame1, text="10-15", command=add1).grid(row=4, column=2)
    Button(frame1, text="20-25", command=add2).grid(row=4, column=3)
    Button(frame1, text="35+", command=add3).grid(row=4, column=5)

    Label(frame2, text="Question: What is Turtle?").grid(row=1, column=4)
    Button(frame2, text="Guided User Interface", command=add1v2).grid(row=4, column=2)
    Button(frame2, text="Module", command=add2v2).grid(row=4, column=4)
    Button(frame2, text="Boolean Value", command=add3v2).grid(row=4, column=5)

    Label(frame3, text="Question: What does the 'Print' command do?").grid(row=1, column=3)
    Button(frame3, text="Create a window", command=add1v3).grid(row=4, column=2)
    Button(frame3, text="Show a message in the Python Shell", command=add2v3).grid(row=4, column=3)
    Button(frame3, text="Print to the printer", command=add3v3).grid(row=4, column=5)


    Label(frame4, text="Question: What does the 'Print' command do?").grid(row=1, column=3)
    Button(frame4, text="Create a window", command=add1v4).grid(row=4, column=2)
    Button(frame4, text="Show a message in the Python Shell", command=add2v4).grid(row=4, column=3)
    Button(frame4, text="Print to the printer", command=add3v4).grid(row=4, column=5)

    notebook.pack()

    Label(root, text="Your Answers:").pack()

    #Label(root, text="Your Answers:").pack()
    #Label(root, textvariable=user_answers).pack()

    #Label(root, text="Total:").pack()
    #Label(root, textvariable=total2).pack()

    #Label(root, text ="Total:").pack()
    #Label(root, textvariable=total3).pack()

#For Question 1:
def add1():
    Label(frame1, text="+1pts").grid(row=1, column=6)
    counter1()

def add2():
    Label(frame1, text="+2pts").grid(row=1, column=6)
    counter2()

def add3():
    Label(frame1, text="+3pts").grid(row=1, column=6)
    counter3()

#For Question 2:
def add1v2():
    Label(frame1, text="+1pts").grid(row=1, column=6)
    counter4()

def add2v2():
    Label(frame1, text="+2pts").grid(row=1, column=6)
    counter5()

def add3v2():
    Label(frame1, text="+3pts").grid(row=1, column=6)
    counter6()

#For Question 3:
def add1v3():
    Label(frame1, text="+1pts").grid(row=1, column=6)
    counter7()

def add2v3():
    Label(frame1, text="+2pts").grid(row=1, column=6)
    counter8()

def add3v3():
    Label(frame1, text="+3pts").grid(row=1, column=6)
    counter9()

#For Question 4:
def add1v4():
    Label(frame1, text="+1pts").grid(row=1, column=6)
    counter10()

def add2v4():
    Label(frame1, text="+2pts").grid(row=1, column=6)
    counter11()

def add3v4():
    Label(frame1, text="+3pts").grid(row=1, column=6)
    counter12()

'''def correct2():
    #Label(frame2, text="Correct").grid(row=1, column=6)
    #counter()

def incorrect2():
    #Label(frame2, text="Incorrect").grid(row=1, column=6)

def correct3():
    #Label(frame3, text="Correct").grid(row=1, column=6)
    #counter()

def incorrect3():
    Label(frame3, text="Incorrect").grid(row=1, column=6)

    #after "correct/incorrect#3, have a message that shows overall user progression based on questions correct"

def correct4():
    Label(frame4, text="Correct").grid(row=1, column=6)
    counter()

def incorrect4():
    Label(frame4, text="Incorrect").grid(row=1, column=6)
    counter()'''

#For Q#1:
def counter1():
    Label(root).pack()
    Label(root, textvariable=user_answers).pack()
    user_answers.set(user_answers.get() + "a")

def counter2():
    Label(root).pack()
    Label(root, textvariable=user_answers2).pack()
    user_answers2.set(user_answers2.get() + "b")

def counter3():
    Label(root).pack()
    Label(root, textvariable=user_answers3).pack()
    user_answers3.set(user_answers3.get() + "c")



#For Q#2:
def counter4():
    Label(root).pack()
    Label(root, textvariable=user_answers4).pack()
    user_answers4.set(user_answers4.get() + "a")

def counter5():
    Label(root).pack()
    Label(root, textvariable=user_answers5).pack()
    user_answers5.set(user_answers5.get() + "b")

def counter6():
    Label(root).pack()
    Label(root, textvariable=user_answers6).pack()
    user_answers6.set(user_answers6.get() + "c")



#For Q#3:
def counter7():
    Label(root).pack()
    Label(root, textvariable=user_answers7).pack()
    user_answers7.set(user_answers7.get() + "a")

def counter8():
    Label(root).pack()
    Label(root, textvariable=user_answers8).pack()
    user_answers8.set(user_answers8.get() + "b")

def counter9():
    Label(root).pack()
    Label(root, textvariable=user_answers9).pack()
    user_answers9.set(user_answers9.get() + "c")



#For Q#4:
def counter10():
    Label(root).pack()
    Label(root, textvariable=user_answers10).pack()
    user_answers10.set(user_answers10.get() + "a")

def counter11():
    Label(root).pack()
    Label(root, textvariable=user_answers11).pack()
    user_answers11.set(user_answers11.get() + "b")

def counter12():
    Label(root).pack()
    Label(root, textvariable=user_answers12).pack()
    user_answers12.set(user_answers12.get() + "c")


root = Tk()

user_answers = StringVar()  # defaults to 0
user_answers2 = StringVar()
user_answers3 = StringVar()
user_answers4 = StringVar()
user_answers5 = StringVar()
user_answers6 = StringVar()
user_answers7 = StringVar()
user_answers8 = StringVar()
user_answers9 = StringVar()
user_answers10 = StringVar()
user_answers11 = StringVar()
user_answers12 = StringVar()
#total2 = IntVar()
#total3 = IntVar()

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)

main()

root.mainloop()