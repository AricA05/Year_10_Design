from tkinter import * #GUI package

window = Tk() #window
window.title("Practice option menu") #creates a title for window
window.geometry('700x600+0+0') #sizeing of window
header = Label(window, text="This is an option menu example!", font=("arial",30,"bold"), fg="steelblue").pack() 
#Label type = header with font and colour modifications


exercise = StringVar(window)#OptionMenu this also sets "exercise" as the term for the option menu
exercise.set('----') #sets option menu to --- by default


#List of exercises to choose from for option menu list
Exercise = {'Plank', 'Push-up', 'Run','Lunge'}

exercise = OptionMenu(window, exercise, *Exercise) 
#creates the menu, and window that option menu is in gets passed the list of choices for the optionmenu (*Exercise) 
exercise.place(x=220,y=105)#placement of the optionmenu

window.mainloop()