from tkinter import *
win=Tk()
win.configure(bg="#F3E4A4") # 
def add():
    re.delete(0,END) # 
    add1=int(op1.get()) # 
    add2=int(op2.get()) # 
    re.insert(INSERT,add1+add2)
op1=Entry(win,width=5,relief="groove") # 
op1.grid(row=0,pady=20)
Label(win,text="+",bg="#F3E4A4").grid(row=0,column=1)
op2=Entry(win,width=5,relief="groove") # 
op2.grid(row=0,column=2)
Label(win,text="=",bg="#F3E4A4").grid(row=0,column=3)
re=Entry(win,width=5,relief="groove") # 
re.grid(row=0,column=4)
Button(win,text="",command=add,relief="groove",bg="#10C9F5").grid(row=1,
 columnspan=5, ipadx=10)
win.mainloop()