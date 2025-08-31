from tkinter import *
win=Tk()
Label(win,text=":",font=14).grid(pady=10,row=0,column=0)
Entry(win,show="*").grid(row=0,column=1) # 
Label(win,text=":",font=14).grid(pady=10,row=1,column=0)
Entry(win,show="*").grid(row=1,column=1) # 
win.mainloop()