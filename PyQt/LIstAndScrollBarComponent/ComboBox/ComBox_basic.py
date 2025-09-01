from tkinter import *
from tkinter.ttk import * # ttk

win = Tk()
val = StringVar() # ，
fruits = ("", "", "", "") # 
Combobox(win, textvariable=val, values=fruits).pack(padx=10, pady=10)
win.mainloop()