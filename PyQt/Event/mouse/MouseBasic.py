def show1(event):
    # 
    label.config(text="Label")

def hidden1(event):
    # 
    label.config(text="")

from tkinter import *

win=Tk()
label=Label(win, bg="#C5E1EF",width=20, height=3)

label.pack(pady=20, padx=20)
label.bind("<Enter>", show1) # 
label.bind("<Leave>", hidden1) # 

win.mainloop()