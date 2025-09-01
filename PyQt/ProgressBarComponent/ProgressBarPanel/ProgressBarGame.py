from tkinter import *
from tkinter.ttk import *

val = 0
def add1(c):
    global val
    val += c
    # 
    if val > pro["max"]:
        label.config(text="")
    else:
        vari.set(val)

win = Tk()
win.geometry("220x190")

Label(win, text=": ").grid(row=0, column=0, columnspan=1)
# ，2，1
Button(win, text="", command=lambda: add1(1)).grid(row=0, column=1, pady=10)
Button(win, text="", command=lambda: add1(2)).grid(row=0, column=2, pady=10)
img = PhotoImage(file="../../CanvasComponent/CanvasPonent/cat.png")  # 
label = Label(win, image=img, compound=TOP, foreground="red")
label.grid(row=1, column=0, columnspan=4)

vari = IntVar()  # 
vari.set(0)
# 
pro = Progressbar(win, mode="determinate", variable=vari, max=50, length=200)
pro.grid(row=2, column=0, columnspan=4, pady=5)
win.mainloop()