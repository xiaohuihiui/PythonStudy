from tkinter import *
from tkinter.ttk import * # ttkSeparator，ttk

win = Tk()
win.title("1")
win.configure(background="#AFEBE5")

sty1 = Style()  # 
sty1.configure("BW.TLabel", foreground="#fff", background="red")

sty2 = Style() # 
sty2.configure("BW.TFrame", background="#AFEBE5")
win.geometry("250x200")
win.configure(bg="#AFEBE5")

# ，
left = Frame(win, style="BW.TLabel", width=260)
left.pack(side=LEFT)

# 、
Label(left, text="2024-03-08", background="red", foreground="#fff").pack()
Label(left, text="06:49", background="red", foreground="#fff").pack()
Label(left, text=" Fri", background="red", foreground="#fff").pack()


# 
Label(left, text="", background="red", foreground="#fff").pack(ipady=5)
Label(left, text="", background="red", foreground="#fff").pack(ipady=5)
Separator(left, orient=HORIZONTAL).pack(side=TOP, fill=X)

# ，
Label(left, text="", background="red", foreground="#fff").pack(ipady=5)
Label(left, text="", background="red", foreground="#fff").pack(ipady=5)

# ，
right = Frame(win, width=260, style="BW.TFrame")
right.pack(side=LEFT)
Label(right, text="", background="#AFEBE5", justify="center", wraplength=100, font=16).pack(padx=40)
win.mainloop()