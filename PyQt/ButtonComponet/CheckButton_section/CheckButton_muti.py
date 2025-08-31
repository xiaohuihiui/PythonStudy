from tkinter import *

win = Tk()
# 
fruits = ("apple", "banana", "cherry")
for i in fruits:
    val = IntVar()
    checkbox1 = Checkbutton(win, variable=val, text=i).pack(side=LEFT)
win.mainloop()