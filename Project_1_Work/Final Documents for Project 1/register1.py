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