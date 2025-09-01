def gettext(event):
    str = ""  # ，
    index1 = fruites.curselection()  # 
    # for
    for item in index1:
        str += fruites.get(item) + ","
    label.config(text="" + str)

from tkinter import *

win = Tk()
win.configure(bg="#F5D7C4")  # 
win.geometry("240x240")  # 
label = Label(win, height=5, wraplength=190, justify="left", bg="#F1DAA1", relief="groove")
label.pack(side="top", fill="x", padx=10, pady=10)

scr1 = Scrollbar(win)  # 

# 
listitem = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

# yscrollcommand
fruites = Listbox(win, height=7, yscrollcommand=scr1.set, selectmode="multiple", justify="center", width=30)
for i in listitem:
    fruites.insert(END, i)  # 
fruites.pack(side="left", fill="x")

fruites.bind("<<ListboxSelect>>", gettext)

scr1.pack(side="left", fill="y")
scr1.config(command=fruites.yview)

win.mainloop()