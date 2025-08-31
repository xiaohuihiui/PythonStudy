# OptionMenu
from tkinter import *

win = Tk()  # 
win.geometry("150x220")
win.title("OptionMenu")
Label(text=":").pack(fill="x", anchor="w")

# 
list = ('---', '---', '---', '---', '---', '---', '---')

v = StringVar(win)

# "*" + ，
om = OptionMenu(win, v, *list).pack(fill="x")

win.mainloop()