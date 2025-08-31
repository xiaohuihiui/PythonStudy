from tkinter import *

win = Tk()
win.geometry("360x180")
for i in range(6):  #
    if i % 2 == 0:
        #
        Frame(bg="#B1FFBB", width=60, height=40, cursor="cross").grid(row=0, column=i, pady=10)
    else:
        #
        Frame(bg="#FFD9C5", width=60, height=40, cursor="plus").grid(row=0, column=i, pady=20)
win.mainloop()