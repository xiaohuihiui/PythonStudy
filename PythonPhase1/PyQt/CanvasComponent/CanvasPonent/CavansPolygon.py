from tkinter import *

win = Tk()
win.title("")
win.geometry("240x260")
canvas = Canvas(win, width=250, height=250, relief="solid")

poly1=canvas.create_polygon(27,8,27,62,54,34,fill="#fbfe0d") #
poly2=canvas.create_polygon(54,34,81,8,81,63,fill="red") #
poly3=canvas.create_polygon(81,63,54,35,25,61,53,90,fill="#0001fc") #
poly4=canvas.create_polygon(81,63,81,176,138,121,fill="#32ccfe") #
poly5=canvas.create_polygon(81,97,43,135,81,174,fill="#fdcbfe") #
poly6=canvas.create_polygon(139,119,60,198,140,198,fill="#02cd02") #
poly7=canvas.create_polygon(140,198,167,170,223,170,196,198,fill="#9b01ff") #

canvas.pack()
win.mainloop()