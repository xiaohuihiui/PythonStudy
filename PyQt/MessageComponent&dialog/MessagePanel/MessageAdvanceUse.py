# 0: , 1: , 2: , 3: , 4: 
def coll():
    a=randint(0,6)  # 
    mess.config(fg="#f00")  # ，
    if a==0:
        text = ""
    elif a==1:
        text = ""
    elif a==2:
        text = ""
    elif a==3:
        text = ""
    elif a==4:
        text = ""
    else:
        text = ","  # ，
        mess.config(fg="#000")
    val.set("\n"+text+"\n")
    mess.pack()

from tkinter import *
from random import *

win=Tk()
win.geometry("300x230")
win.title("")

val=StringVar()  # valMessage
# Message
mess=Message(win,textvariable=val,font=14,aspect=350,fg="red")
Button(win,text="",command=coll).pack(side=TOP)

win.mainloop()