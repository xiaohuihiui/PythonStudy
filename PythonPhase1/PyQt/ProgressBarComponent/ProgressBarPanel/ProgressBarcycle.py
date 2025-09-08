
from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("")

# 
img = PhotoImage(file="../../CanvasComponent/CanvasPonent/cat.png")
label=Label(win, image=img,text="", foreground="red",
font=("", 18),compound=BOTTOM)
label.grid(row=1, column=0, columnspan=3)

pro = Progressbar(win, mode="indeterminate", value=0, max=100, length=100)
pro.grid(row=2, column=0, columnspan=3, pady=10)

# ，
Button(win, text="", command=pro.start(200), width=7).grid(row=4, column=0, padx=5)

win.mainloop()