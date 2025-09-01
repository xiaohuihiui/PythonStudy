# 
def result1():
    if v.get() == 1:
        re.config(text="，，“ () ”")
    else:
        re.config(text="，“ () ”")

from tkinter import *

win = Tk()
win.title("")  # 
win.geometry("300x150") # 

text = Label(win, text="，", font="14").pack(anchor=W)

# 
v = IntVar()
ans1 = Radiobutton(win, text="", variable=v, value=1, selectcolor="#F1D4C9")
ans1.pack(anchor=W)
ans2 = Radiobutton(win, text="", variable=v, value=2, selectcolor="#F1D4C9")
ans2.pack(anchor=W)

button = Button(win, text="", command=result1, font="14", bg="#F1C57E", relief="groove").pack()

re = Label(win)  # Label
re.pack()
win.mainloop()