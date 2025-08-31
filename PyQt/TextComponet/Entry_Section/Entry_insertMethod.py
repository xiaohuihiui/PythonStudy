from tkinter import *
win=Tk()
Label(win,text=":").grid(row=0,column=0)
entry=Entry(win,relief="groove")
entry.insert(0,"admin") # 
entry.grid(row=0,column=1)
win.mainloop()