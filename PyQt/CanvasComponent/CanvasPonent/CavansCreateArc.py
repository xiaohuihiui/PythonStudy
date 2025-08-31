from tkinter import *

win = Tk()
win.title("")
win.geometry("300x200")
canvas = Canvas(win, width=500, height=400, relief="solid")
canvas.create_arc(20,40,150,150,extent=120,outline="#EDB17A",start=30,width=2, style=ARC)
canvas.create_arc(170,40,300,150,extent=120,outline="#EDB17A",start=30, width=2,style=CHORD)
canvas.create_arc(320,40,450,150,extent=120,outline="#EDB17A",start=30,width=2, style=PIESLICE)
canvas.pack()
win.mainloop()