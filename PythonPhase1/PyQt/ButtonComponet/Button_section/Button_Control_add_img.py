def show():
    # Label，
    Label(win, image=img).pack()

from tkinter import *

win = Tk()
img = PhotoImage(file="logo.png")   # 
but1 = Button(win, text="add picture", command=show).pack() # 
win.mainloop()
