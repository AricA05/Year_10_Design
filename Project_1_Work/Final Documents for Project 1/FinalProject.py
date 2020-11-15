#import modules
import tkinter as tk
import os
import sqlite3 as sq #For tables and database
import datetime
# Designing window for registration
 

def register():
    #get inputted username and password
    username_info = entun.get()
    password_info = entpw.get()
    #opens file in write mode
    file = open(username_info + ".txt", "w")
    #write username and password information into file
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    #clears inputted username and password
    entun.delete(0, "end")
    entpw.delete(0, "end")

    #label shows signup success on screen
    labregsuccess = tk.Label(root, text="Registration Success - Please Login", fg="green", font=("calibri", 11))
    labregsuccess.pack()


def login():
    
    #gets username and password
    username1 = entun.get() + ".txt"
    password1 = entpw.get() 
    
    #unhashtag the below lines to show that program (in terminal) prints the username and password, essentially shows how it reads each line if code
    #print(username1)
    #print(password1)

    #clears fields
    entun.delete(0, "end")
    entpw.delete(0, "end")
    
    #The method listdir() returns a list containing the names of the entries in the directory given by path
    list_of_files = os.listdir()
    #defining verification's conditions 
    if username1 in list_of_files:
        file1 = open(username1, "r")#open the file in read/txt mode
        
        #reads file, splitlines() on the "newline" character, so the newline character is not left hanging at the end of each line
        verify = file1.read().splitlines()
        #unhashtag the below line to have terminal print the method of how it verifies the username and password, using the splitline
        #print(verify)
        if password1 in verify:
            home()
 
        else:
            invalid_password()
    else:
        unknown_user()



def home():
    labsuccess = tk.Label(root, text = "Login Successful", fg = "green")
    labsuccess.pack()
    import homepage



def invalid_password():
    labinvalidpass = tk.Label(root, text = "Invalid Password", fg = "red", font = ("Calibri", 11))
    labinvalidpass.pack()


def unknown_user():
    labunknowuser = tk.Label(root, text = "Unknown User", fg = "red")
    labunknowuser.pack()


        
root = tk.Tk()

labun = tk.Label(root,text = "User Name: ")
entun = tk.Entry(root, width = 20)

labpw = tk.Label(root,text = "Password: ")
entpw = tk.Entry(root, width = 20, show = "*")

labun.pack()
entun.pack()

labpw.pack()
entpw.pack()

#This button makes a new user
btnRegister = tk.Button(root,text = "Register", fg = "blue",command = register)
btnLogin = tk.Button(root, text = "Login", fg="green", command = login)

btnRegister.pack()
btnLogin.pack()


root.mainloop()
