from tkinter import *

win = Tk()
labelFrame = LabelFrame(win, text="")  # LabelFrame
labelFrame.grid(row=0, ipadx=10, ipady=10, column=1)
hero = StringVar()
hero.set("")
# 
Radiobutton(labelFrame, variable=hero, text="", value="").grid(row=1, column=1)
Radiobutton(labelFrame, variable=hero, text="", value="").grid(row=2, column=1)
Radiobutton(labelFrame, variable=hero, text="", value="").grid(row=3, column=1)
Radiobutton(labelFrame, variable=hero, text="", value="").grid(row=4, column=1)
win.mainloop()