def pop1():
    # win.winfo_x()win.winfo_y()win
    menu2_2.post(win.winfo_x()+60, win.winfo_y()+120)

from tkinter import *
win=Tk()
menu1=Menu(win) # 
menu2_1=Menu(menu1,tearoff=False) # 
menu1.add_cascade(label="",menu=menu2_1) # 
menu2_1.add_command(label="") # 
menu2_1.add_command(label="")
menu2_1.add_command(label="")
menu2_1.add_command(label="")
menu2_1.add_command(label="")
menu1.add_command(label="",command=pop1)
menu2_2=Menu(menu1,tearoff=False) # 
menu2_2.add_command(label="")
menu2_2.add_command(label="")
menu1.add_command(label="",command=win.quit)
win.config(menu=menu1)
win.mainloop()