from tkinter import *
from tkinter.ttk import *

win = Tk()

note = Notebook(win, width=300, height=200)

pane1 = Frame()  # 
img1 = PhotoImage(file="cat.png")
Label(pane1, image=img1).pack()  # 
Label(pane1, text=",").pack(pady=20)
Button(pane1, text="", state="DISABLE").pack()

pane2 = Frame()  # 
img2 = PhotoImage(file="1.png")  # 
Label(pane2, image=img2).pack()
Label(pane2, text=",")
Button(pane2, text="", state="DISABLE").pack()
note.add(pane1, text="") # 
note.add(pane2, text="") # 

note.pack()
win.mainloop()