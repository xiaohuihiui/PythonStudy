# Toplevel
from tkinter import *

def begin():
    # 2，
    win2 = Toplevel()  # 
    win2.geometry("200x120")  # 
    win2.configure(bg="#FFACAB")  # 
    win2.title("")  # 
    Label(win2, text="，！", font=14, bg="#FFACAB").pack(pady=50)

def change():
    # 
    win2 = Toplevel()
    win2.geometry("200x120")
    win2.configure(bg="#FFACAB")
    win2.title("2")
    Label(win2, text="2", bg="#FFACAB", font=14, width=35).pack(side="top", fill="x")
    Label(win2, text="，！", bg="#FFACAB", font=16).pack(pady=20, side="top", fill="x")

win1 = Tk()
win1.geometry("270x220")
win1.title("1")
win1.configure(bg="#FFCD63")
# 1
label = Label(win1, text="1", background="#FFFFB5", font=14, width=35)
label.grid(row=0, column=0, columnspan=5, ipady=8)

btn1 = Button(win1, text="", background="#35A837", command=begin)
btn1.grid(row=2, column=1, pady=10)

btn2 = Button(win1, text="", background="#FF4A4F", command=change)
btn2.grid(row=2, column=3, pady=10)

win1.mainloop()