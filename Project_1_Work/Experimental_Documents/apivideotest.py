import tkinter as tk 
import requests


def clicked():
    results = requests.get('https://wger.de/api/v2/exercisecomment/?limit=20&offset=60')
    results_json = results.json()
    for p in results_json['results']:
    	print(p['comment'])


root = tk.Tk()
root.geometry('100x100')

btn1 = tk.Button(root, text='click me', command = clicked)
btn1.pack()



root.mainloop()