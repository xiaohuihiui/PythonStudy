from tkinter import *

win = Tk()
val1 = IntVar()
checkbox1 = Checkbutton(win, variable=val1, text="app").pack()  # 
val2 = IntVar()  # 
checkbox2 = Checkbutton(win, variable=val2, text="ba").pack()  # 
win.mainloop()