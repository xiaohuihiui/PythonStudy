from tkinter import *
from PIL import Image,ImageTk
win=Tk()
win.title("")
img=Image.open("gwc.jpg")
img=ImageTk.PhotoImage(img)
label=Label(win,image=img).grid(row=0,column=1)
win.mainloop()
