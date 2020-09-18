import tkinter as tk

print("Stage 5")
'''
Base 2 to Base 10
1010 
1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 1 * 8 + 0 * 4 + 1 * 2 + 0 * 1 = 10
'''
#This gets printed in terminal when program is opened

#This function makes program process the entered value
#*args function: when function is called, *args allows any number of parameters to pass through it by ignoring any value typed in the box
#"process"will show up in terminal when code is ran to show that code is being excecuted 
#NOTE:A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.
def process(*args):
	
#ent_value is the entry widget (tk.Entry widget), .get acts on ent_value and gets the value
	val = ent_value.get()
	


	#Check to ensure string of 1's and 0's
	check = check01(val)
	


	if (check == True):
		#removes left most 0 val gets passed to "def remove0 function"
		val = remove0(val)
		#converts from base 2 to base 10
		result = base2to10(val)
		#updates display with conversion
		lab_results.config(text = str(val) + " --> " + str(result))
	else:
		lab_results.config(text = "INVALID")

	ent_value.delete(0,tk.END)

def base2to10(str):

	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
		total = total + int(str[i]) * 2**n
		n = n + 1

	return total

#function for removing left most 0's
def remove0(str):

	'''012345 -- this is the index number of the string (6 index values total in this example)
 	   000101 -- this is the inputted string/value, the "for i in range" will identify the first "1" and return/enter once identified in this case, it will take the last three digits'''

#examines each index of the number inputted in the string and determines when the first 1 appears. If no 1's are found it has to be a zero. 
	for i in range(0, len(str),1):
	#if str at index "i" is equivalent to a "1" (if there is a number "1" in the string...)
		if (str[i] == "1"):
			return str[i:]#returns index "i" to the length of the string (returns whatever number where after the first "1")
	
	#if you make it past this loop:		
	return str

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