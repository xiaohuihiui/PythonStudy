from tkinter import *
from tkinter.ttk import * # ttk

def setdat(a):
    temp = monsel.get()
    if temp == 2:
        dat["value"] = tuple(range(1, 29))
    elif temp == 4 or temp == 6 or temp == 9 or temp == 11:
        dat["value"] = tuple(range(1, 31))
    else:
        dat["value"] = tuple(range(1, 32))
def get1():
    if len(entry.get()) == 0:  # 
        return False
    else:
        # 
        h = str(horsel.get()) if horsel.get() > 10 else "0" + str(horsel.get())
        m = str(minsel.get()) if minsel.get() > 10 else "0" + str(minsel.get())
        item1 = (str(mon.get()) + "" + str(datsel.get()) + "", h + ":" + m, entry.get())
        if not tree.focus() == "":  # 
            # ，
            tree.insert("", tree.index(tree.focus()), values=item1)
            del1()
        else:
            tree.insert("", END, values=item1)
            reset1()

def del1():
    # ，
    if tree.focus() == "":
        return False
    else:
        tree.delete(tree.focus())
def edt(a):
    temp = tree.set(tree.focus())
    d = temp["date"].split("")  # “”
    t = temp["time"].split(":")  # “:”
    monsel.set(int(d[0]))  # 
    datsel.set(int(d[1].split("")[0]))  # 
    horsel.set(int(t[0]))  # 
    minsel.set(int(t[1]))  # 
    entry.delete(0, END)
    entry.insert(INSERT, temp["depart"])
def reset1():
    monsel.set(1)
    datsel.set(1)
    horsel.set(0)
    minsel.set(0)
    entry.delete(0, END)


win = Tk()
# 
frame = Frame()
frame.grid()
Label(frame,text="：").grid(row=0,column=0)
monsel = IntVar() # 
monsel.set(1)
mon = Combobox(frame, value=tuple(range(1, 13)), textvariable=monsel, width=5) # 
mon.grid(row=0, column=1)
mon.bind("<<ComboboxSelected>>", setdat) # ，
Label(frame,text="-").grid(row=0, column=2)
datsel = IntVar() # 
datsel.set(1)
dat = Combobox(frame, value=tuple(range(1, 32)), textvariable=datsel, width=5) # 
dat.grid(row=0, column=3)
Label(frame, text="：").grid(row=0, column=4, columnspan=2, sticky=S + E)
horsel = IntVar() # 
horsel.set(0)
hor = Spinbox(frame, from_=0, to=24, width=5, textvariable=horsel) # 
hor.grid(row=0, column=6)
Label(frame, text=":").grid(row=0, column=7)
minsel = IntVar()
minsel.set(0) # 
min = Spinbox(frame, from_=0, to=59, width=5, textvariable=minsel) # 
min.grid(row=0, column=8)
Label(frame, text="：").grid(row=0, column=9) # 
entry = Entry(frame)
entry.grid(row=0, column=10)
Button(frame, text="", command=get1).grid(row=0, column=11)
Button(frame, text="", command=del1).grid(row=0, column=12)
# Treeview
tree = Treeview(win, column=("date", "time", "depart"), show="headings")
tree.heading("date", text="") # 
tree.heading("time", text="")
tree.heading("depart", text="")
tree.grid(row=1, column=0)
tree.bind("<<TreeviewSelect>>", edt) # ，edt()
win.mainloop()