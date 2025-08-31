from tkinter import *

win = Tk()
win.title("")
win.geometry("300x200")
canvas = Canvas(win, width=500, height=400, relief="solid")

canvas.create_line(95,124,95,194,fill="#E9D39D",capstyle=ROUND,width=12) #
canvas.create_arc(5,-70,185,162,extent=-40,outline="#32E143",fill="#32E143",
start=-70,width=2,style=PIESLICE) # 
canvas.create_arc(8,-67,181,155,extent=-40,outline="#E92742",fill="#E92742",
start=-70,width=2,style=PIESLICE) # 
canvas.create_arc(92,74,97,79,extent=159,fill="#000",width=2,style=ARC) #
canvas.create_arc(97,94,102,99,extent=180,start=90,fill="#000",width=2,style=ARC) #
canvas.create_arc(110,124,113,127,extent=359,fill="#000",width=2,style=ARC) #
canvas.create_arc(90,134,93,137,extent=359,fill="#000",width=2,style=ARC) #

canvas.pack()
win.mainloop()