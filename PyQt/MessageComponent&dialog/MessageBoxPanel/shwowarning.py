def mess():
    # showwarning()
    showwarning("", "，，")

from tkinter import *
from tkinter.messagebox import *

win=Tk()
win.title("")

# ，，
Button(win, text="", command=mess).pack(padx=20, pady=20)
win.mainloop()