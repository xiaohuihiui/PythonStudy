from tkinter import *
from tkinter.ttk import * # ttk

win = Tk()
# 
tree=Treeview(win)
tree.heading("#0",text="")
tree.insert("","0","wei",text="")
shu=tree.insert("","1",text="")
wu=tree.insert("","2",text="")
tree.insert("wei","0",text="") # wei
tree.insert(shu,"0",text="") # shu
tree.insert(wu,"0",text="sunxuan") # shu
tree.pack()
win.mainloop()