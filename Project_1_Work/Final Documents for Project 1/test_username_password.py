#import modules
 
from tkinter import *
import os
import sqlite3 as sq #For tables and database
import datetime
# Designing window for registration
 
def signup():
    global signup_screen
    signup_screen = Toplevel(main_screen)#Top level is used simply as a frame, so it supports other pop up windows
    signup_screen.title("Sign Up")#title 
    signup_screen.geometry("300x250")#sizing of screen
 
    global username
    global password
    global username_entry
    global password_entry

    #sets text variables
    username = StringVar()
    password = StringVar()
 
    Label(signup_screen, text="Please enter details below", bg="blue", fg = "white").pack()
    username_label = Label(signup_screen, text="Create Username").pack()#instructions for user
    username_entry = Entry(signup_screen, textvariable=username)#entry idget used to display single line of text entered by user
    username_entry.pack()
    password_label = Label(signup_screen, text="Create Password").pack()
    password_entry = Entry(signup_screen, textvariable=password, show='*')
    password_entry.pack()
    Button(signup_screen, text="Sign Up", width=10, height=1, bg="blue", command = signup_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def signup_user():
    #get inputted username and password
    username_info = username.get()
    password_info = password.get()
    #opens file in write mode
    file = open(username_info, "w")
    #write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    #clears inputted username and password
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    #label shows signup success on screen
    Label(signup_screen, text="Registration Success - Please Close Window and Login", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    #gets username and password
    username1 = username_verify.get()
    password1 = password_verify.get()
    #clears fields
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    #The method listdir() returns a list containing the names of the entries in the directory given by path
    list_of_files = os.listdir()
    #defining verification's conditions 
    if username1 in list_of_files:
        file1 = open(username1, "r")#open the file in read/txt mode
        
        #reads file, splitlines() on the "newline" character, so the newline character is not left hanging at the end of each line
        verify = file1.read().splitlines()
        if password1 in verify:
            window()
 
        else:
            invalid_password()
    else:
        unknown_user()
#window if login is successfull
 
def window():
    global window
    import Project1Final
    


'''global window
    window = Toplevel(login_screen)#window
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
    L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)'''


def invalid_password():
    global login_screen
    Label(login_screen, text="Invalid Password or User Not Found", fg="red", font=("calibri", 11)).pack()

def unknown_user():
    global login_screen
    Label(login_screen, text="Invalid Password or User Not Found", fg="red", font=("calibri", 11)).pack()


# Designing Main(first) window
 
def main_screen():
    global main_screen
    main_screen = Tk() #creates mainscreen window
    main_screen.geometry("300x250") #config's window size
    main_screen.title("Account Login")#window title
    #create form label, tells user to eithr login or register
    Label(text="Select Your Choice", bg="blue", fg="white", width="300", height="2", font=("Calibri", 13)).pack()
    #create login button
    Button(text="Login", height="2", width="30", command = login).pack()  
    #create register button
    Button(text="Register", height="2", width="30", command=signup).pack()
 
    main_screen.mainloop()
 
 
main_screen()