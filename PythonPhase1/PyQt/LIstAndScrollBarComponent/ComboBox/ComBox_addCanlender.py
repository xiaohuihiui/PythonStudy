from tkinter import *
from tkinter.ttk import *


# 
def getMon(a):
    items = monOption.get()
    # 4，6，9，11，30
    if items == "4" or items == "6" or items == "9" or items == "11":
        b = tuple(range(1, 31))
    elif items == "2":
        b = tuple(range(1, 29))  # 2，28
    else:
        b = tuple(range(1, 32))  # 31

    dateOption["values"] = b


# ，
def getDate():
    info = label3.cget("text")
    temp = monOption.get() + "" + dateOption.get() + ", \t" + text.get("0.0", END)
    label3.config(text=info + temp)
    text.delete("0.0", END)


win = Tk()
win.title("")

number = StringVar()
# 1-12
a = tuple(range(1, 15))  # 
monOption = Combobox(win, width=5, textvariable=number, values=a)
monOption.current(0)  # 1
monOption.grid(row=0, column=1, sticky=E, columnspan=2)

# Combobox，，getMon()
monOption.bind("<<ComboboxSelected>>", getMon)  # ，getMon()

label1 = Label(win, text="").grid(row=1, column=2, sticky=W)

# 31
b = tuple(range(1, 32))  # 
dateOption = Combobox(win, width=5, values=b)  # 
dateOption.grid(row=1, column=3, pady=10, columnspan=2)
dateOption.current(0)  # 1

label2 = Label(win, text="").grid(row=1, column=5, sticky=W)
text = Text(win, width=40, height=10)  # 
text.grid(row=2, columnspan=8)

button = Button(win, text="", command=getDate).grid(row=3, columnspan=8)

label3 = Label(win)
label3.grid(row=4, columnspan=8)
win.mainloop()