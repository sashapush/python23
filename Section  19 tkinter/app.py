import tkinter as tk #alias import
from tkinter import ttk
#tk._test()

def greet():
    print(f"Hello {user_name.get() or 'World'}") #.get() is called on tk.StringVar object to retrieve the contents of the variable


root = tk.Tk() #create Tk object from tk package
root.title("Hello")
tk.Label(root, text = "Label Left", bg="green").pack(side="left", expand=True, fill="both")
tk.Label(root, text = "Label 1", bg="green").pack(side="left", fill="both", expand =True)  #expand -allows to expand space on resize
#fill - fills the label on the axis, taking as much space as available; First label takes priority if fill by axis is used
tk.Label(root, text = "Label 2", bg="red").pack(side="top", fill="both") #there's also fill="both", but elements conflict with each other if both have both.
user_name = tk.StringVar() #object used to track entry widget

name_label = ttk.Label(root,text="Name:")
name_label.pack(side="left",padx=(0,10))
name_entry = ttk.Entry(root, width=15,textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root,text="Greetings", command=greet) #(where to put it, and what to run)
greet_button.pack(side='left', fill="x", expand=True) #.pack is used to put component in the window

quit_button = ttk.Button(root, text="Quit", command=root.destroy) #destroy app when interaction happens
quit_button.pack(side="left",fill="x",expand=True)
root.mainloop()
