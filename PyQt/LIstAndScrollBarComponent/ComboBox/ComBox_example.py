from tkinter import *
from tkinter.ttk import * # ttk

win = Tk()
win.title("Combobox")

label1 = Label(win, text="：").grid(row=1, column=0, columnspan=2, pady=10)

# 
item = ("", "", "", "", "", "")

# 
useroption = Combobox(win, width=12, values=item)
useroption.grid(row=1, column=2, pady=10) # 
useroption.current(0) # 0item

label2 = Label(win, text="：").grid(row=2, pady=10, columnspan=2)

# 
numberChosen = Combobox(win, width=12, values=("", "", "", "", ""))
numberChosen.grid(row=2, column=2, pady=10)
numberChosen.current(0)

button = Button(win, text="").grid(row=3, columnspan=4, pady=10)
win.mainloop()