from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime #for proper date/time formatting 
import os #operating system 
window = Tk() #makes window
window.title("Welcome!") #window title 
window.geometry('855x600+0+0') #dimensions for window size
header = Label(window, text="Workout Tracker", font=("arial",30,"bold"), bg="orange").pack()
#Label type = header with font and colour modifications

window.configure(bg='lightblue') #configures background colour (bg)


con = sq.connect('workout.db') #sqlite database 
c = con.cursor() #The cursor allows to call on the ‘execute’ method, which will allow for SQL commands 
#'execute' method will allow for a table to be created based off the selected exercise from option menu

L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100) 
#all of these are different label's pretty much just simple writing, all correspond to below entry boxes
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)

#defining option menu 1
exercise = StringVar(window)#definition for 1st option menu, the actual widget isn't created until line 43
exercise.set('----') #blank dropdown menu setting
#defining option menu 2
exercisedb = StringVar(window)#definition for 2nd option menu, the actual widget isn't created until line 47
exercisedb.set('----')

#StringVariables are used in this program, so changes to inputted fields can be changed and monitored
day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
Reps = StringVar(window)
Sets = StringVar(window)

#List of names for drop down list
Exercise = {'Plank', 'Lunge', 'BicepCurl', 'Other'}
# *Exercise is the dictionary (created on line 41)
exercised = OptionMenu(window, exercise, *Exercise) #For 1st drop down list 
exercised.place(x=220,y=105)

# *Exercise is the dictionary (the one that's created on line 41)
exercisedbase = OptionMenu(window, exercisedb, *Exercise)#For 2nd drop down list
exercisedbase.place(x=100,y=500)

#Entry/text 'T' boxes, 'textvariable' refers to the defined string variables on lines 34-38
#Textvariables allow user to input any values, therefore the user input is not 'restricted'in their inputs in any way
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

#executed when 'submit' button is hit - this command sends inputted data to database
def record():
        print("You have submitted a record")#prints in terminal - helps signify the command that is running
        #'IF NOT EXISTS' is used to basically check if there is an existing table or not, in this case there is, as they have been premade in the dbbrowser
        #Exercise.get is used to 'isolate' the data for the chosen exercise from the first option menu
        # 'c' is defined in line 15, which is made so 'execute' methods can be used
        c.execute('CREATE TABLE IF NOT EXISTS ' +exercise.get()+ ' (Datestamp TEXT, Reps INTEGER, Sets INTEGER)') 
        
        date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #required format for 'import datetime'
        #INSERT INTO is used to nsert new records into a table                                          the '?' is used for when where we want to substitute an integer for the inputted date, reps, or sets
        c.execute('INSERT INTO ' +exercise.get()+ ' (Datestamp, Reps, Sets) VALUES (?, ?, ?)',
                  (date, Reps.get(), Sets.get())) #sumbits record into database.
        con.commit() #saves/commits changes 

#Resets fields for option menu#1 after submit
        exercise.set('----')
        day.set('')
        month.set('')
        year.set('')
        Reps.set('')
        Sets.set('')

#Clears boxes when 'clear' button is hit - this is seperate from when 'submit' is hit
def clear():
    exercise.set('----')
    exercisedb.set('----')
    day.set('')
    month.set('')
    year.set('')
    Reps.set('')
    Sets.set('')

#executed when user wants to 'open file'/retrieve their inputted data    
def get():
    c.execute('SELECT * FROM ' +exercisedb.get()) #Select from which ever exercise is selected
    #this is the frame for the listbox, it is placed in the main window
    frame = Frame(window)
    frame.place(x= 500, y = 270)
    #creating listbox widget, dimesions, placement 
    Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    #tkinter Scrollbar widget creation, this goes on side of 'frame'
    scroll = Scrollbar(frame, orient = VERTICAL) #scrollbar lists box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Date, Reps, Sets') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(window, text = exercisedb.get()+ '      ', 
               font=("arial", 16)).place(x=500,y=210) # Title of data table of exercise/workout file, tilte changes depending on exercise chosen

    L8 = Label(window, text = "They are ordered from most recent", 
               font=("arial", 16)).place(x=500,y=240)
    con.commit()



button_1 = Button(window, text="Submit",command=record)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",command=clear)
button_2.place(x=10,y=400)

button_3 = Button(window,text="Open File",command=get)
button_3.place(x=10,y=500)



import requests


def onclick1():
    results = requests.get('https://wger.de/api/v2/muscle/')
    results_json = results.json()
    for i in results_json['results']:
        print(i['name'])#name is the "Key", terminal output are the "Valves"



def onclick2():
    results = requests.get('https://wger.de/api/v2/exercisecomment/?limit=20&offset=60')
    results_json = results.json()
    for p in results_json['results']:
        print(p['comment'])#Comment is the "Key", terminal output are the "valves"


btnapi1 = Button(window, text = "Click for Muscle Categories", fg = "blue",highlightbackground="Orange",command = onclick1)
btnapi1.place(x=480,y=100)


btnapi2 = Button(window, text = "Click for tips on how to exercise these muscles", fg = "orange",highlightbackground="Orange",command = onclick2)
btnapi2.place(x=480,y=180)


def showquiz():
    import quizsection

btnquiz = Button(window, text = "CLICK FOR QUIZ TO EVALUATE YOUR PROGRESS",fg="blue", height=5, highlightbackground = "Orange", highlightthickness = 5, command = showquiz)
btnquiz.place(x=480,y=430)



window.mainloop() #mainloop() = make sure that window stays open

