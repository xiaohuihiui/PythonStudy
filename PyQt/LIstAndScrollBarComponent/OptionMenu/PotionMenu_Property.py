# OptionMenu
from tkinter import *

def result():
    # 
    if v.get() == items[2]:
        re.config(text="")
    else:
        re.config(text="，"+items[2])

win = Tk()
win.title("")  # 
win.configure(bg="#ffffcc")

# OptionMenu
text = Text(win, width=50, height=13, bg="#ffffcc", font=14, relief="flat")

# 
ques = "，，、、、，：\n\n\n：。\n\n\n：。\n\n\n：。\n\n\n：。\n\n\n，？\n\n"
text.insert(END, ques)  # 
text.grid(row=1, columnspan=4)
text.config(state="disabled") # 

# 
items = ("", "", "", "")
v = StringVar(win)
v.set(items[0])  # 
om = OptionMenu(win, v, *items)
om.grid(row=2, columnspan=2)

button = Button(win, text="", command=result).grid(row=2, column=1, columnspan=2)

re = Label(win, padx=5, pady=5, width=60)
re.grid(row=3, column=0, columnspan=3)

win.mainloop()