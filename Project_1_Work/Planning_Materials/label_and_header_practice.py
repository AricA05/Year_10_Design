from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime


window = Tk()
window.title("Practice Labeling and Title's") 
window.geometry('700x600+0+0')
header = Label(window, text="This is a header/title example!", font=("arial",30,"bold"), fg="steelblue").pack()

window.configure(bg='skyblue')

L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100)
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)

window.mainloop()