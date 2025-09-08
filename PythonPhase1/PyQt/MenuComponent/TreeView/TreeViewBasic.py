from tkinter import *
from tkinter.ttk import * # 

win = Tk()

# 
tree = Treeview(win, columns=("hero", "type", "operate"), show="tree headings", displaycolumns=(0,1,2))
# 
tree.heading("hero", text="", anchor="center")
tree.heading("type", text="", anchor="center")
tree.heading("operate", text="", anchor="center")
# 
tree.insert("",END,values=("","","5"))
tree.insert("",END,values=("","","3"))
tree.insert("",END,values=("","","3"))
tree.insert("",END,values=("","","3"))
tree.pack()
win.mainloop()