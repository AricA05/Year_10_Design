from tkinter import * #GUI package
window = Tk()
window.title("button practice code") 
window.geometry('500x300+0+0')
header = Label(window, text="button practice", font=("arial",30,"bold"), fg="steelblue").pack()

window.configure(bg='skyblue')

L1 = Label(window, text = "click button", font=("arial", 18)).place(x=10,y=100)

#window = Tk()

def new_winF(): # new window definition
    newwin = Toplevel(window)
    display = Label(newwin, text="window opened from button click")
    display.pack()    

button1 =Button(window, text ="this is a button", command =new_winF)#command linked
button1.place(x=200,y=140)

window.mainloop()