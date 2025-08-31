from tkinter import *
win=Tk()
def back():
    length=len(op1.get()) # b
    op1.delete(length-1, END) #   #KEYWORD
op1=Entry(win,relief="groove")
op1.insert(INSERT, "") # 
op1.grid(row=0)
Button(win,text="",command=back).grid(row=0,column=1)
win.mainloop()