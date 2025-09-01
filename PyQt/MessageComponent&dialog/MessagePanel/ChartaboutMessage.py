i=0  # Message

def mess():
    textLeft=enc.get()  # 
    global i
    # ，
    Message(box, text=textLeft, bg="#CBEDE9", width=140).grid(row=i, column=0, sticky="W")
    # 
    Message(box, text="："+textLeft, bg="#EFE2B8", width=140).grid(row=i+1, column=2)
    i += 2  # 

from tkinter import *

win=Tk()
win.geometry("300x230")  # 

box=Frame(width=300,height=200)  # ，
box.place(x=0,y=0)

info=Frame(width=250,height=20)  # ，
info.place(x=40,y=200)

enc=Entry(info)  # 
enc.pack(side=LEFT,fill=BOTH)

btn=Button(info,text="",command=mess).pack(side=LEFT)  # 

win.mainloop()