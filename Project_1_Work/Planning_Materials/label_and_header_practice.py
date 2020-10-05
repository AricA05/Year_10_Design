from tkinter import * #GUI package

window = Tk() #window
window.title("Practice Labeling and Title's") #creates a title for window
window.geometry('700x600+0+0') #sizeing of window
header = Label(window, text="This is a header/title example!", font=("arial",30,"bold"), fg="steelblue").pack() 
#Label type = header with font and colour modifications

window.configure(bg='skyblue') #configures background colour (bg) of window

L1 = Label(window, text = "Exercise", font=("arial", 18)).place(x=10,y=100) 
#all of these are different label's pretty much just simple writing 
L2 = Label(window, text = "Day (dd)", font=("arial",18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)", font=("arial",18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)", font=("arial",18)).place(x=10,y=250)
L5 = Label(window, text = "Reps per set ", font=("arial",18)).place(x=10,y=300)
L6 = Label(window, text = "Sets completed", font=("arial",18)).place(x=10,y=350)

window.mainloop() 
'''runs the Tkinter event loop, waits for any action to occur on page, 
proccess' action/event as long as window isn't closed'''