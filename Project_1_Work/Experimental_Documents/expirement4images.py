# importing only those functions 
# which are needed 
import tkinter as tk
from tkinter.ttk import *
  
# creating tkinter window 

def ShowPhoto():
    canvas = tk.Canvas(root, width = 700, height = 600, bg = "black")
    canvas.pack(expand = tk.YES, fill = tk.BOTH)
    # Adding widgets to the root window 
    Label1 = tk.Label(root, text = 'GeeksforGeeks', font = ('Verdana', 15))
    Label1.pack()
    # Creating a photoimage object to use image 
    photo = tk.PhotoImage(file = r"weight1.png") 
  
# here, image option is used to 
# set image on button 

root = tk.Tk() 

Button1 = tk.Button(root, text = 'Click Me !', command = ShowPhoto)
Button1.pack()
  
root.mainloop()