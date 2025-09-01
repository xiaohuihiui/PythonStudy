def fgl():
    button.config(fg="red")  # 

def bg(event):
    button.config(bg="#ABE1DB")  # 

def font(event):
    button.config(font="14")  # 

from tkinter import *
win=Tk()
button=Button(win,text="",command=fgl)  # fgl()
button.bind("<Button-1>",bg,add="+")  # bg()

button.bind("<Button-1>",font,add="+")  # font()
button.pack(pady=10)
win.mainloop()