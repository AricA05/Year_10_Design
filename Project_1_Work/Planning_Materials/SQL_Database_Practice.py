from tkinter import * #GUI package
import sqlite3 as sq #For tables and database
import datetime


con = sq.connect(tbd) #sqlite database 
c = con.cursor()#Cursor allows you to invoke methods that,
#execute SQLite statements, such as fetch data from the result sets etc...'''


#get function gets the text entered in the entry boxes and submits it to database
def get():
        print("You have submitted a record")#prints in terminal 
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +____.get()+ ' (Datestamp TEXT, TBD(exercise) INTEGER, TBD(reps) INTEGER)')
        #execute inserts in SQL table in this case, it will also create a SQL table based of the datestamp and the enetred integers
        #the .get here will come from one of the dropdown menu's possibly
        date = datetime.date(int(year.get()),int(month.get()), int(day.get())) #required format for 'import datetime',
        #this will create the date and time colum or row in th SQL database, that can be displayed when data is called by users

        c.execute('INSERT INTO ' +______.get()+ ' (Datestamp, TBD(Exercise), TBD(reps?))) ',
        #this will get another one of the entered values from the chosen textbox and insert it into SQL database
                  (date, ______.get(), ______.get())) #sumbits record into database.
        con.commit()
        #saves the changes


#Resets fields after submit
        day.set('')
        month.set('')
        year.set('')
        ____.set('')
        ______.set('')

#Clears boxes when submit button is hit
def clear():
    day.set('')
    month.set('')
    year.set('')
    _____.set('')
    ______.set('')