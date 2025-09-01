from tkinter import *
from tkinter.ttk import *

win = Tk()
tree = Treeview(win, columns=("date", "temperature"))
tree.heading("#0", text="")  # 
tree.heading("date", text="")
tree.heading("temperature", text="")
rain = PhotoImage(file="rainheardly.png")  # 
storm = PhotoImage(file="storm.png")
sunny = PhotoImage(file="sunny.png")
tree.insert("", END, values=("41", "-3~5"), image=rain, text="") # 
tree.insert("", END, values=("42", "-3~7"), image=sunny, text="")
tree.insert("", END, values=("43", "0~8"), image=storm, text="")
tree.insert("", END, values=("44", "1~10"), image=sunny, text="")
tree.insert("", END, values=("45", "2~10"), image=sunny, text="")
tree.insert("", END, values=("46", "2~12"), image=sunny, text="")
tree.insert("", END, values=("47", "2~10"), image=rain, text="")
tree.pack()
win.mainloop()