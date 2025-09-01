from tkinter import *
from tkinter.ttk import * # ttk

win = Tk()
# 
tree = Treeview(win,columns=("score"))
# 
tree.heading("#0",text="",anchor=W)
tree.heading("score",text="",anchor=W)
# 
score1={"R001":"20","R002":"19","R003":"19","R004":"16"}
score2={"B001":"17","B002":"19","B003":"18","B004":"14"}
score3={"G001":"17","G002":"15","G003":"16","G004":"16"}
# 、，
red=tree.insert("",END,text="",open=True)
blue=tree.insert("",END,text="")
green=tree.insert("",END,text="")
# 
for index,item in score1.items():
    tree.insert(red,END,text=index,values=(item))
for index,item in score2.items():
    tree.insert(blue,END,text=index,values=(item))
for index,item in score3.items():
    tree.insert(green,END,text=index,values=(item))

tree.pack()
win.mainloop()