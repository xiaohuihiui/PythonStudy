from tkinter import *
import random

#
fill_color = ["#B0E3DD", "#E19644", "#6689E1", "#E16678", "#66E1CA"]
#
font_family = ["", "", "", "", "", "", "", ""]
def draw():
    canvas.delete("all")  #
    color = fill_color[random.randint(0, 4)]  #
    family = font_family[random.randint(0, 7)]  #
    text = canvas.create_text(160, 60, text=str, font=(family, 20), fill=color)  #

win = Tk()
win.title("")
win.geometry("330x200")
canvas = Canvas(win, width=300, height=160, relief="solid")
str = ""  #
canvas.pack()
Button(win, text="", command=draw).pack()
win.mainloop()