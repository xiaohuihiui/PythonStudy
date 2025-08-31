# Toplevel
def creat():
    top=Toplevel()
    top.geometry("150x150")
    top.title("")
    top.configure(bg="#D8EBB8")
    Label(top, text="Toplevel").pack()

from tkinter import *
win1 = Tk()
win1.geometry("200x200")  # 
win1.configure(bg="#F7D7C4")  # 

Button(win1, text="", command=creat).pack()

win1.mainloop()