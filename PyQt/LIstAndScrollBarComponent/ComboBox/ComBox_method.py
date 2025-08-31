def set1():
    combobox1.set("128") # 

def get1():
    str = combobox1.get() # 
    label.config(text="！"+str+"")
    label.grid(row=2, column=0, columnspan=3)

from tkinter import *
from tkinter.ttk import *

win = Tk()
Label(win, text="：").grid(row=0, column=0)
val2 = StringVar()
combobox1 = Combobox(win, textvariable=val2)

# 
combobox1["values"] = ("38", "58", "88", "128")
combobox1.current(0)  # 
combobox1.grid(row=0, column=1, pady=10)

Button(win, text="", command=set1).grid(row=0, column=2)
Button(win, text="", command=get1).grid(row=1, column=0, columnspan=3, pady=10)

label = Label(win, foreground="red", font=14)
win.mainloop()