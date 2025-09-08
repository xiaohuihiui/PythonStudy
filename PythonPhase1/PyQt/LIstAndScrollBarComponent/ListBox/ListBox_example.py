# bind()，，，:
def show(event):
    for i in items:
        listbox.insert(END, i)  # 
    listbox.pack(fill=X)

from tkinter import *

win = Tk()
win.title("Listbox") # 

win.geometry("180x150")  # 

# 
listbox = Listbox(win, bg="#FFF8DC", selectbackground="#D15FEE", selectmode="multiple", height=5, width=25)

items = ["", "", "", "", "", ""] # 

enc = Entry(win)  # 
enc.pack(fill=X)

# ，，show()
enc.bind("<Button-1>", show)
win.mainloop()