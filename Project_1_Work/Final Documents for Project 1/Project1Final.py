from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime

window = Tk() #window
window.title("Welcome!") #winodw title 
window.geometry('800x600+0+0') #dimensions for window size
header = Label(window, text="Workout Tracker", font=("arial",30,"bold"), bg="orange").pack()
#Label type = header with font and colour modifications

window.configure(bg='lightblue') #configures background colour (bg)

con = sq.connect('workout.db') #sqlite database 
c = con.cursor() #sqlite command-this connects code to database


L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100) 
#all of these are different label's pretty much just simple writing 
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)


#variables for each list
exercise = StringVar(window)#1st dropdown 
exercise.set('----') #blank dropdown menu setting

exercisedb = StringVar(window)#2nd dropdown list
exercisedb.set('----')

day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
Reps = StringVar(window)
Sets = StringVar(window)

#List of names for drop down list
Exercise = {'Plank'}

exercised = OptionMenu(window, exercise, *Exercise) #For 1st drop down list 
exercised.place(x=220,y=105)

exercisedbase = OptionMenu(window, exercisedb, *Exercise)#For 2nd drop down list
exercisedbase.place(x=100,y=500)

#Entry for 'input' in GUI
dayT = Entry(window, textvariable=day)
dayT.place(x=220,y=155)

monthT = Entry(window, textvariable=month)
monthT.place(x=220,y=205)

yearT = Entry(window, textvariable=year)
yearT.place(x=220,y=255)

RepsT = Entry(window, textvariable=Reps)
RepsT.place(x=220,y=305)

SetsT = Entry(window, textvariable=Sets)
SetsT.place(x=220,y=355)

#get function gets the text entered in the entry boxes and submits it to database
def get():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +exercise.get()+ ' (Datestamp TEXT, Reps INTEGER, Sets INTEGER)')
        
        date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #required format for 'import datetime'

        c.execute('INSERT INTO ' +exercise.get()+ ' (Datestamp, Reps, Sets) VALUES (?, ?, ?)',
                  (date, Reps.get(), Sets.get())) #sumbits record into database.
        con.commit()

#Resets fields after submit
        exercise.set('----')
        day.set('')
        month.set('')
        year.set('')
        Reps.set('')
        Sets.set('')

#Clears boxes when submit button is hit
def clear():
    exercise.set('----')
    exercisedb.set('----')
    day.set('')
    month.set('')
    year.set('')
    Reps.set('')
    Sets.set('')
    
def record():
    c.execute('SELECT * FROM ' +exercisedb.get()) #Select from which ever exercise is selected

    frame = Frame(window)
    frame.place(x= 500, y = 150)
    
    Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) #scrollbar lists box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Date, Reps, Sets') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(window, text = exercisedb.get()+ '      ', 
               font=("arial", 16)).place(x=500,y=100) # Title of data table of exercise/workout file, tilte changes depending on exercise chosen

    L8 = Label(window, text = "They are ordered from most recent", 
               font=("arial", 16)).place(x=500,y=350)
    con.commit()

button_1 = Button(window, text="Submit",command=get)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",command=clear)
button_2.place(x=10,y=400)

button_3 = Button(window,text="Open File",command=record)
button_3.place(x=10,y=500)


window.mainloop() #mainloop() = make sure that window stays open

