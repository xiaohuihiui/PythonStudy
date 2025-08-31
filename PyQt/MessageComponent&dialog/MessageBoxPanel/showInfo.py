def mess():
    showinfo("welcome!", ",") # showinfo()

from tkinter import *
from tkinter.messagebox import * # messagebox

win=Tk()
win.title("")

# ，，
Button(win, text="", command=mess).pack(padx=20, pady=20)
win.mainloop()