import tkinter as tk

print ("Stage 2")
#This gets printed in terminal when program is opened

#This function makes program process the entered value
#*args function: when function is called, *args allows any number of parameters to pass through it by ignoring any value typed in the box
#"process"will show up in terminal when code is ran to show that code is being excecuted 
#NOTE:A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.
def process(*args):
	print("process")

	#ent_value is the entry widget (tk.Entry widget), .get acts on ent_value and gets the value
	#print(val) prints the entered number into terminal
	val = ent_value.get()
	print(val)

#Checks to insure string of only 1's and 0's is entered in box




#If val is valid (just 1's and 0's) 
   #Removes left most zero's 
   #Does conversion
   #updates display with conversion
#else: updates display with error message

	
	#takes entry widget and delete everything from first character to lat character (essentially when enter is hit the box resets to blank)
	ent_value.delete(0,tk.END)

#root creates wndow in which prgram is in
root = tk.Tk()

lab_instructions = tk.Label(root, text = "Enter Binary")
'''first widget: label widget, goes into tk module and uses constructor module that will build a label'''
'''The first parameter is where it will be placed, in this case it is placed in the root window'''
'''after first parameter (root), named parameters can be used to create the text of the label(in this case we use text)'''
ent_value = tk.Entry(root)
'''second widget: entry widget, goes into tk module and creates entry box'''
'''Only attached to root window, does not need any name parameters'''
lab_results = tk.Label(root, text = "--")
'''third widget: label widget, creates another label'''
'''Attached to root window, name parameter is used for results'''

lab_instructions.pack()
'''takes lab_instructions widget and packs it into root window, it knows to pack it into
root window because it is specified as the parameter above. The must be done for ent_value and lab_results'''
ent_value.pack()
lab_results.pack()





#root.bind...process: this binds the process function in line 9-10 to the return key
root.bind("<Return>", process)
'''sets up a mainloop for program that allows it to stay open and wait to be used'''
root.mainloop()

