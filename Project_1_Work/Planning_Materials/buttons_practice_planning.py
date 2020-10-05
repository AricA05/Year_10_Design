from tkinter import * #GUI package
window = Tk() #window
window.title("button practice code") #winodw title 
window.geometry('500x300+0+0') #dimensions for window size
header = Label(window, text="button practice", font=("arial",30,"bold"), fg="steelblue").pack()
#Label type = header with font and colour modifications

window.configure(bg='skyblue') #configures background colour (bg)

L1 = Label(window, text = "click button", font=("arial", 18)).place(x=10,y=100)
#more practice with label creation and fonts/text 


def new_winF(): # new window definition
    newwin = Toplevel(window)#opens new window 
    display = Label(newwin, text="window opened from button click")#displayed in new window
    display.pack() 

button1 =Button(window, text ="this is a button", command =new_winF)#command linked
button1.place(x=200,y=140)#placement of button

window.mainloop()#tkinter event loop