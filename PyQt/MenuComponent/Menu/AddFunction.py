from tkinter import *
from tkinter.messagebox import *
i = 84
# 1，1
def wrong():
    global i
    i -= 1
    label.config(text=i)

# 
def suc():
    top = Toplevel(win) # 
    Label(top, text=",!\n,"+str(i), fg="red").grid(row=0, column=0, padx=10, pady=10)
# 
def help():
    showwarning("", "4")

# 
def game():
    boo = askyesnocancel("", "，，，")
    if boo == True:
        i = 0
        label.config(text=i)  # ，0
    elif boo==False:
        i=84
        label.config(text=i)  # ，
win = Tk()
win.title("")
menu1 = Menu(win)  # 
# 
menu1.add_command(label="", command=game)
menu1.add_command(label="", command=help)
menu1.add_command(label="", command=win.quit)
win.config(menu=menu1)  # 
for c in range(6):
    for j in range(14):
        Button(win, text="", width=1, command=wrong).grid(row=c, column=j)

Button(win, text="", width=1, command=suc).grid(row=3, column=3)
label = Label(win, font=14, fg="red", text=84)
label.grid(row=8, column=0, columnspan=14)

win.mainloop()
