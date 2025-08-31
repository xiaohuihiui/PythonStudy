from tkinter import *
win=Tk()
def show():
    str=entry.get() # 
    print(str) # 
entry=Entry(win) # Entry
entry.grid(row=0)
Button(win,text="",command=show).grid(row=0,column=1) # 
win.mainloop()