from tkinter import *
from tkinter.ttk import *

# 
def max_win(event):
    win.geometry("600x400")

# 
def normal_win(event):
    win.geometry("300x200")

# 
def txt():
    global val
    global font_size
    global top
    top = Toplevel(win) # 
    val = StringVar()
    val.set("") # 
    font_family = ("", "", "", "", "", "")

win = Tk()
win.geometry("300x200")
menu1 = Menu(win)  # 

menu2_1 = Menu(menu1)  # 
menu1.add_cascade(label="", menu=menu2_1)  # 

menu2_1.add_command(label="", accelerator="Ctrl+Up", command=lambda :max_win(""))
menu2_1.add_command(label="", accelerator="Ctrl+Down", command=lambda :normal_win(""))  # 
menu2_1.add_command(label="", command=win.iconify)

menu2_1.add_separator()  # 
menu2_1.add_command(label="", command=win.quit)  # ，

menu2_2 = Menu(menu1, tearoff=0)  # 
menu1.add_cascade(label="", menu=menu2_2)  # 
menu2_2.add_command(label="", command=txt)  # 
win.config(menu=menu1)
label = Label(win, text="")
label.grid(row=0, column=0)
win.bind_all("<Control-Up>", max_win)
win.bind_all("<Control-Down>", normal_win)
win.mainloop()