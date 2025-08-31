from tkinter import *
from tkinter.messagebox import *

# ，
def draw(event):
    canvas.coords(bird, event.x, event.y)

# 
def panduan(event):
    x1=abs(event.x-340)
    y1=abs(event.y-70)
    if x1<70 and y1<75:
        showinfo("", "")

win = Tk()
win.title("")
win.geometry("400x320")
canvas = Canvas(win, width=400, height=320, relief="solid", bg="#E7D2BB")
bird1 = PhotoImage(file="bird.png")
house1 = PhotoImage(file="house.png")
house = canvas.create_image(340, 70, image=house1)  #
bird = canvas.create_image(150, 250, image=bird1)  #

canvas.grid(row=0, column=0, columnspan=2)
canvas.bind("<B1-Motion>", draw)  #
canvas.bind("<ButtonRelease-1>", panduan)  #

win.mainloop()