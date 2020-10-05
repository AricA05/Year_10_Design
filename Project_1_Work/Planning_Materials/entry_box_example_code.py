from tkinter import * #GUI package

window = Tk() #window
window.title("Practice Entry Boxes") #creates a title for window
window.geometry('700x600+0+0') #sizeing of window
header = Label(window, text="This is an Entry Box example!", font=("arial",30,"bold"), fg="steelblue").pack() 

window.configure(bg='skyblue')

L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100) 
#all of these are different label's pretty much just simple writing 
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)

exercise = StringVar(window)#OptionMenu this also sets "exercise" as the term for the option menu
exercise.set('----') #sets option menu to --- by default

day = StringVar(window)#these are the entry boxes
month = StringVar(window)
year = StringVar(window)
Reps = StringVar(window)
Sets = StringVar(window)

#List of exercises to choose from for option menu list
Exercise = {'Plank', 'Push-up', 'Run','Lunge'}

exercise = OptionMenu(window, exercise, *Exercise) 
#creates the menu, and window that option menu is in gets passed the list of choices for the optionmenu (*Exercise) 
exercise.place(x=220,y=105)#placement of the optionmenu

#Entry boxes created allows users to enter data
day = Entry(window) #these all corresspond/connect to the window's created on line 24 - 28
day.place(x=220,y=155)#placement of the entry boxes

month = Entry(window) 
month.place(x=220,y=205)

year = Entry(window)
year.place(x=220,y=255)

Reps = Entry(window)
Reps.place(x=220,y=305)

Sets = Entry(window)
Sets.place(x=220,y=355)

window.mainloop()