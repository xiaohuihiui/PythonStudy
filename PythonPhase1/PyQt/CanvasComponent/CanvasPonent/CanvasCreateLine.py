from tkinter import *

win=Tk()
win.title("")
win.geometry("300x200")
canvas=Canvas(win,width=200,height=200) #
# 
line1=(14,65,66,65,83,19,99,64,148,64,111,96,126,143,83,123,44,142,58,97,14,65)
line1=canvas.create_line(*line1,fill="red") #
canvas.pack()
win.mainloop()