from tkinter import *

win = Tk()
items = ["", "", "", "", "", ""]  # 
listbox = Listbox(win, height=6, width=20, relief="solid")  # 
for i in items:  # for
    listbox.insert(END, i)

listbox.pack()
win.mainloop()