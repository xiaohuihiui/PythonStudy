from tkinter import *
win=Tk() # 
win.title("") # 
Label(win,text=":").grid(row=0,column=0,pady=10)
# 
Spinbox(win,values=("","","")).grid(row=0,column=1,pady=10)
Label(win,text=":").grid(row=1,column=0,pady=10)
# from_to
Spinbox(win,from_=1,to=5).grid(row=1,column=1,pady=10)
Label(win,text="5").grid(row=1,column=2,pady=10)
Label(win,text=":").grid(row=2,column=0,pady=10)
Spinbox(win,values=("","","")).grid(row=2,column=1,pady=10)
win.mainloop()