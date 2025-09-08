from tkinter import *

win = Tk()
val = StringVar()  # ，OptionMenu
# : 、
optionmenu = OptionMenu(win, val, "", "", "", "")
optionmenu.pack()
win.mainloop()