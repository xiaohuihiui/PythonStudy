from tkinter import *
win=Tk()
Spinbox(win,from_=10,to=100).pack()
Spinbox(win,values=("a","b","c")).pack()
win.mainloop()