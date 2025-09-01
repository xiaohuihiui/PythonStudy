def show(ele):
    listbox.pack(fill=X)

# ，
def typeIn(event):
    enc.delete(0, END)
    enc.insert(INSERT, "aa")

from tkinter import *

win = Tk()
win.title("Listbox")
win.geometry("180x150")
val = StringVar()
val.set("     ")  # 
listbox = Listbox(win, bg="#FFF8DC", selectbackground="#2C92DF", selectmode="single", height=6, width=25, listvariable=val)
enc = Entry(win)
enc.pack(fill=X)

# ，，show()
enc.bind("<Button-1>", show)

# ，，typeIn()
listbox.bind("<Double-Button-1>", typeIn)
win.mainloop()