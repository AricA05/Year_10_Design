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

 
 
#For Question 1:
def add1():
    tk.Label(frame1, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text = "A").pack()


def add2():
    tk.Label(frame1, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text = "B").pack()


def add3():
    tk.Label(frame1, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()


#For Question 2:
def add1v2():
    tk.Label(frame2, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()


def add2v2():
    tk.Label(frame2, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()


def add3v2():
    tk.Label(frame2, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()


#For Question 3:
def add1v3():
    tk.Label(frame3, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()


def add2v3():
    tk.Label(frame3, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()


def add3v3():
    tk.Label(frame3, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()


#For Question 4:
def add1v4():
    tk.Label(frame4, text="You chose option A").grid(row=1, column=6)
    tk.Label(screen, text="A").pack()


def add2v4():
    tk.Label(frame4, text="You chose option B").grid(row=1, column=6)
    tk.Label(screen, text="B").pack()


def add3v4():
    tk.Label(frame4, text="You chose option C").grid(row=1, column=6)
    tk.Label(screen, text="C").pack()

 

screen = tk.Tk()
screen.title("Progression Quiz") 


notebook = ttk.Notebook(screen)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)

main()

screen.mainloop()