import tkinter as tk 
import requests


def onclick1():
	results = requests.get('https://wger.de/api/v2/muscle/')
	results_json = results.json()
	for i in results_json['results']:
		print(i['name'])



def onclick2():
	results = requests.get('https://wger.de/api/v2/exercisecomment/?limit=20&offset=60')
	results_json = results.json()
	for p in results_json['results']:
		print(p['comment'])


root = tk.Tk()
root.title("button")
root.geometry("400x100+0+0")

btn1 = tk.Button(root, text = "Click for Muscle Categories", fg = "green", command = onclick1)
btn2 = tk.Button(root, text = "Click for tips on how to exercise these muscles", fg = "blue", command = onclick2)

btn1.pack()
btn2.pack()

root.mainloop()

#https://www.youtube.com/watch?v=l4E1ntsk7rw



'''def onclick2():
	results = requests.get('https://wger.de/api/v2/muscle/')
	results_json = results.json()
	for i in results_json['results']:
		print(i['name'])'''