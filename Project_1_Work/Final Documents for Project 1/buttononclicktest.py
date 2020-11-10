import tkinter as tk 
import requests

def onclick():
	results = requests.get('https://wger.de/api/v2/exercisecomment/?limit=20&offset=60')
	results_json = results.json()
	for p in results_json['results']:
		print(p['comment'])

root = tk.Tk()
root.title("button")

btn = tk.Button(root, text = "button", command = onclick)

btn.pack()

root.mainloop()

#https://www.youtube.com/watch?v=l4E1ntsk7rw