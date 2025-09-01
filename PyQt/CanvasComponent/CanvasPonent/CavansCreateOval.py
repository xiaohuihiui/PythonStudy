from tkinter import *

win = Tk()
win.title("")
win.geometry("300x200")
canvas = Canvas(win, width=200, height=200, relief="solid")

cir1 = canvas.create_oval(34, 68, 143, 127, fill="#C8F7F2") #
cir2 = canvas.create_oval(59,83,71,99,fill="#E6F1B7") #
cir2_1 = canvas.create_oval(61,86,71,94,fill="#000000") #
cir3 = canvas.create_oval(101,83,113,99,fill="#E6F1B7") #
cir3_1 = canvas.create_oval(100,86,109,94,fill="#000000") #

canvas.pack()
win.mainloop()