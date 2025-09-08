def mess():
    # askyesnocancel()
    boo=askyesnocancel("","，“”，“”，“”")
    if boo==True:  # 
        win.quit()
    elif boo==False:  # 
        win.iconify()

from tkinter import *
from tkinter.messagebox import *

win=Tk()
win.title("")

# ，，
Button(win,text="",command=mess).pack(padx=20,pady=20)
win.mainloop()