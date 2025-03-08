import tkinter as tk #alias import
from tkinter import ttk
#tk._test()

def greet():
    print("Hello world")



root = tk.Tk() #create Tk object from tk package
root.title("Hello")

greet_button = ttk.Button(root,text="Greetings", command=greet) #(where to put it, and what to run)
greet_button.pack(side='left', fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy) #destroy app when interaction happens
quit_button.pack(side="left",fill="x",expand=True)
root.mainloop()
