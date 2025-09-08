# |                                |                                 |
# | --------------------------------- | --------------------------------- |
# | `get()`                           |  Spinbox                    |
# | `insert(index, text)`             |  `text`  `index`  |
# | `selection('from', index)`        |  `index`        |
# | `selection('to', index)`          |  `index`        |
# | `selection('range', start, end)`  |  `start`  `end`    |
# | `selection_element(element=None)` |                          |
from tkinter import *
def show():
    # 
    info.insert("insert", "\t:%s%s %s\n" % (spmon.get(), spdat.get(), spwek.get(),))
win = Tk()
win.title("")

mess=Label(win, text=":").grid(row=0,column=0,columnspan=5,pady=10)
spmon=Spinbox(win,from_=1,to=12,width=10) # 
spmon.grid(row=1,column=0,pady=10)
mon=Label(win,text="").grid(row=1,column=1,pady=10)
spdat=Spinbox(win,from_=1,to=30,width=10) # 
spdat.grid(row=1,column=2,pady=10)
dat=Label(win,text="").grid(row=1,column=3,pady=10)
spwek=Spinbox(win,values=("","","","","","",""),width=10) # 
spwek.grid(row=1,column=5,columnspan=3,pady=10)
info=Text(win,bg="#BFEFFF",width=50,height=10) # 
get1 = Button(win, text="",width=30 ,bg="#ED889E",command=show).grid(row=3,
 columnspan=5,pady=10)
info.grid(row=2,columnspan=10)
win.mainloop()