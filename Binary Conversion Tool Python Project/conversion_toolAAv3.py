import tkinter as tk

print("Stage 3")
#This gets printed in terminal when program is opened

#This function makes program process the entered value
#*args function: when function is called, *args allows any number of parameters to pass through it by ignoring any value typed in the box
#"process"will show up in terminal when code is ran to show that code is being excecuted 
#NOTE:A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.
def process(*args):


	#ent_value is the entry widget (tk.Entry widget), .get acts on ent_value and gets the value
	val = ent_value.get()
	
	#Checks to insure string of only 1's and 0's is entered in box
	#this passes the val to the check01 function which is written approx 17 lines below
	check = check01(val)
	#If check is true (only 0's and 1's)
	if (check == True):
		#Window display will show Valid input
		lab_results.config(text = "VALID INPUT")
	else: #If it is not 0's and 1's it will show invalid
		lab_results.config(text = "INVALID")

	#takes entry widget and delete everything from first character to lat character (essentially when enter is hit the box resets to blank)
	ent_value.delete(0,tk.END)

#Function for checking if value is 1's and 0's only
def check01(str):
	
	#Counts number of 0's in the str. (string)
	num_0 = str.count("0")
	num_1 = str.count("1")#counts number of 1's in string

	#if ammount of 1's and 0's is the same as the length of the string (entered value)
	if num_0 + num_1 == len(str):
		return True
	return False

#root creates wndow in which prgram is in
root = tk.Tk()

#Construct the widgets
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

#Configure Widgets

#Add the widgets to the window
lab_instructions.pack()
'''takes lab_instructions widget and packs it into root window, it knows to pack it into
root window because it is specified as the parameter above. The must be done for ent_value and lab_results'''
ent_value.pack()
lab_results.pack()

root.bind("<Return>",process)
root.mainloop()