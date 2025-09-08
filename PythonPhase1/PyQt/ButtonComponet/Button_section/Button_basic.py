from tkinter import *
win=Tk()
Button(win,text="submit").pack(side="left")
img=PhotoImage(file="logo.png")
Button(win,image=img).pack(side="right")
win.mainloop()