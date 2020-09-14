import tkinter as tk

print ("Stage 1")
#This gets printed in terminal when code is ran

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







'''sets up a mainloop for program that allows it to stay open and wait to be used'''
root.mainloop()

