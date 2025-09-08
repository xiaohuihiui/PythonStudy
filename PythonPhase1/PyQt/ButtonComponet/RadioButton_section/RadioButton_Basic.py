from tkinter import *

win = Tk()
vali = IntVar()  # vali
vali.set("male") # male

radio1 = Radiobutton(win, variable=vali, value="male", text="").pack() # 
radio2 = Radiobutton(win, variable=vali, value="female", text="").pack() # 

win.mainloop()