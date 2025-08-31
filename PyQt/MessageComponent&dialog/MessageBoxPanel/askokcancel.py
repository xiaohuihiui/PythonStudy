def mess():
    # askokcancel()
    boo=askokcancel("","，“”")
    if boo==True: # “”
        win.quit() # 

from tkinter import *
from tkinter.messagebox import *

win=Tk()
win.title("")

# ，，
Button(win,text="",command=mess).pack(padx=20,pady=20)
win.mainloop()