import tkinter as tk #alias import
from tkinter import ttk
#tk._test()

def greet():
    print(f"Hello {user_name.get() or 'World'}") #.get() is called on tk.StringVar object to retrieve the contents of the variable



root = tk.Tk() #create Tk object from tk package
root.title("Hello")
user_name = tk.StringVar() #object used to track entry widget

name_label = ttk.Label(root,text="Name:")
name_label.pack(side="left",padx=(0,10))
name_entry = ttk.Entry(root, width=15,textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root,text="Greetings", command=greet) #(where to put it, and what to run)
greet_button.pack(side='left', fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy) #destroy app when interaction happens
quit_button.pack(side="left",fill="x",expand=True)
root.mainloop()
