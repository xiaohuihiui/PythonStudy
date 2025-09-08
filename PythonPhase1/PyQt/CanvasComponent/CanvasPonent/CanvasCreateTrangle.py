def up1(event):
    #
    canvas.move(rect, 0, -2)
def down1(event):
    #
    canvas.move(rect, 0, 2)
def left1(event):
    #
    canvas.move(rect, -2, 0)
def right1(event):
    canvas.move(rect, 2, 0)
from tkinter import *
win = Tk()
win.title("")
win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, relief="solid")  #
rect = canvas.create_rectangle(10, 10, 50, 50, fill="#C8F7F2")  #
canvas.pack()
win.bind("<Up>", up1)  # 
win.bind("<Down>", down1)
win.bind("<Left>", left1)
win.bind("<Right>", right1)
win.mainloop()