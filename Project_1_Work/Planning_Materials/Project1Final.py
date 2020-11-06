from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime

window = Tk() #window
window.title("Welcome!") #winodw title 
window.geometry('700x500+0+0') #dimensions for window size
header = Label(window, text="Workout Tracker", font=("arial",30,"bold"), bg="orange").pack()
#Label type = header with font and colour modifications

window.configure(bg='lightblue') #configures background colour (bg)

L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100) 
#all of these are different label's pretty much just simple writing 
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)







window.mainloop()#tkinter event loop