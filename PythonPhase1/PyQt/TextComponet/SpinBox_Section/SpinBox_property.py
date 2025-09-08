# |                |                               |
# | ----------------- | ------------------------------- |
# | activebackground  |  Spinbox  “active”    |
# | buttonbackground  |                           |
# | buttoncursor      |                     |
# | command           |                |
# | disablebackground |  Spinbox  “disabled”  |                                                                          |
# | ------------------ | ----------------------------------------------------------------------------- |
# | disableforeground  |  Spinbox  “disabled”                                                |
# | exportselection    |                                                              |
# | increment          |  Spinbox                                                         |
# | justify            | Spinbox                                                               |
# | readonlybackground | Spinbox  “readonly”                                                  |
# | state              |  Spinbox ， “normal”（）、“disabled”（）、“readonly”（，） |
# | textvariable       |  tkinter （ StringVar()），，     |
from tkinter import *
win=Tk()
mon=5 # ，5
def typ():
    global mon
    if val.get()=="": # ，
        mon=5
    elif val.get()=="":
        mon=10
    else:
        mon=15
def pay():
    number=int(num.get()) # 
    tatal=number*mon # 
    text1=" "+val.get()+"  "+str(tatal)+" "
    label.config(text=text1)
win.title("")
Label(win,text=":").grid(row=0,column=0,pady=10)
val=StringVar() # Spinbox
val.set("") # 
Spinbox(win,values=("","",""),textvariable=val,
command=typ).grid(row=0,column=1,pady=10)
Label(win,text=":").grid(row=1,column=0,pady=10)

num=Spinbox(win,from_=1,to=5,command=pay)
num.grid(row=1,column=1,pady=10)
Label(win,text="5").grid(row=1,column=2,pady=10)
label=Label(win)
label.grid(row=3,column=0,columnspan=3,pady=10)
win.mainloop()