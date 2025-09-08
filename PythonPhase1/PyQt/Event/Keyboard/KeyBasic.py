def prt(event):
    le = len(text.get("0.0", END))
    label.config(text=str(le))

from tkinter import *

win = Tk()
text = Text(win, width=20, height=5)
text.pack()
label = Label(win)
label.pack()

text.bind("<Key>", prt)  # 

win.mainloop()