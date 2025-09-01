from tkinter import *
from tkinter.ttk import *

win = Tk()
win.title("")

note = Notebook(win, width=250, height=150)  # 
pane1 = Frame()  # 
Button(pane1, text="").pack(pady=20)  # 

pane2 = LabelFrame()
Checkbutton(pane2, text="", variable=StringVar()).pack(pady=20)

pane3 = Frame()
Button(pane3, text="").pack(pady=20)

note.add(pane1, text="")    # 
note.add(pane2, text="")      # 
note.add(pane3, text="Internet") # 

note.pack()
win.mainloop()
