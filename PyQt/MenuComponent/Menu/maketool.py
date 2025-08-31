from tkinter import *
from tkinter.messagebox import *
# 
num = 0

# 
idiom = ["", "", "", "", "", "", "", "", "", "", ""]
idiom_means = ["，", "", "，", "，，", "，", "，", "，", "", "", "", "，", "，"]

# 
def panduan():
    global num
    a = entry.get()
    if a == idiom[num]:
        num += 1
        if (num > len(idiom)):
            boo = askyesno("", "!，？")
            if boo == True:
                num = 0
                panduan()
            else:
                win.quit()
        entry.delete(0, END)
        means.config(text=idiom_means[num])
        level.config(text=" " + str(num + 1) + " ")
# 
def next1(event):
    global num
    num += 1
    panduan()

# ，0
def restart(event):
    global num
    num = 0
    panduan()

# 
def show1():
    showinfo("", "，")

# 
def tip():
    str=idiom[num][0]
    entry.delete(0,END)
    entry.insert(0,str)
win = Tk()
win.geometry("250x200")
win.title("")

# 
menu1 = Menu(win)  # 
menu2_1 = Menu(menu1)  # 
menu1.add_cascade(label="", menu=menu2_1)  # 
menu2_1.add_command(label="", command=lambda:next1(""), accelerator="Ctrl+N")
menu2_1.add_command(label="", command=lambda:restart(""), accelerator="Ctrl+R")
menu2_1.add_separator()  # 
menu2_1.add_command(label="", command=win.quit)  # ,

menu2_2 = Menu(menu1)  # 
# 
menu1.add_cascade(label="", menu=menu2_2)

menu2_2.add_command(label="", command=show1)  # 
menu2_2.add_command(label="", command=tip)  # 

win.config(menu=menu1)
# 
level = Label(win, font=14, text=" 1 ")  # 
level.grid(row=0, column=0, columnspan=4, sticky="E")

means = Label(win, text=idiom_means[0], font=14, width=30, bg="#D8F3F0", height=3, wraplength="200")  # 
means.grid(row=1, column=0, pady=10, columnspan=4)

entry = Entry(win, font=14)  # 
entry.grid(row=2, column=1, sticky="E")

btn = Button(win, text="", command=panduan).grid(row=2, column=2)

win.bind_all("<Control-n>", next1)  # 
win.bind_all("<Control-r>", restart)  # 

win.mainloop()